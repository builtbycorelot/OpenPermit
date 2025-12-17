"""Matrix bot integration for OpenPermit.

This module contains a asyncio-friendly bot that can create permit-specific
rooms, send JSON-LD events, validate inbound payloads against SHACL shapes,
and surface Remote Inspection API hooks for media threads.
"""
from __future__ import annotations

import asyncio
import json
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, Optional
from urllib.parse import urlparse
import re

from nio import (  # type: ignore
    AsyncClient,
    JoinError,
    LoginResponse,
    MatrixRoom,
    RoomMessageText,
)
from pyld import jsonld
from pyshacl import validate
from rdflib import Graph

from remote_inspection.api import PhotoInspectionAPI

from .message_schemas import EVENT_CONTEXT, EVENT_TYPES, build_event_payload

LOGGER = logging.getLogger(__name__)


@dataclass
class MatrixBotConfig:
    """Configuration for connecting to Conduit/Matrix homeserver."""

    homeserver: str
    user: str
    password: str
    device_id: str | None = None
    server_name: str | None = None
    base_room_alias: str = "openpermit"
    permit_room_prefix: str = "permit"
    shapes_file: Path = Path(__file__).parent / "shapes" / "permit.shacl.ttl"
    inspection_api: PhotoInspectionAPI | None = None


class MatrixPermitBot:
    """Matrix bot that manages permit rooms and structured messaging."""

    def __init__(self, config: MatrixBotConfig) -> None:
        self.config = config
        self.client = AsyncClient(
            config.homeserver, config.user, device_id=config.device_id
        )
        self.inspection_api = config.inspection_api or PhotoInspectionAPI()

    async def login(self) -> LoginResponse:
        LOGGER.info("Logging into Matrix homeserver %s", self.config.homeserver)
        resp = await self.client.login(self.config.password)
        if isinstance(resp, LoginResponse):
            LOGGER.info("Matrix login succeeded for %s", self.config.user)
            return resp
        raise RuntimeError(f"Failed to login: {resp}")

    async def ensure_room(self, permit_id: str) -> str:
        """Create or join a room dedicated to a permit.

        The room alias is derived from the permit identifier to make it easy for
        humans to discover from Element clients while keeping the namespace
        scoped to this deployment.
        """

        alias_localpart = self._sanitize_alias(f"{self.config.permit_room_prefix}-{permit_id}")
        alias_full = f"#{alias_localpart}:{self._server_name}"
        LOGGER.debug("Ensuring room exists for %s", permit_id)
        create_resp = await self.client.room_create(
            alias=alias_localpart,
            name=f"Permit {permit_id}",
            topic="OpenPermit application workspace",
            is_direct=False,
        )

        if hasattr(create_resp, "room_id"):
            LOGGER.info("Created room %s for permit %s", create_resp.room_id, permit_id)
            return create_resp.room_id  # type: ignore[return-value]

        # Room may already exist - join it
        LOGGER.debug("Attempting to join room alias %s", alias_full)
        join_resp = await self.client.join(alias_full)
        if isinstance(join_resp, JoinError):
            raise RuntimeError(f"Unable to join room for permit {permit_id}: {join_resp}")
        LOGGER.info("Joined existing room %s for permit %s", join_resp.room_id, permit_id)
        return join_resp.room_id  # type: ignore[return-value]

    async def send_event(self, room_id: str, event_type: str, content: Dict[str, Any]) -> None:
        if event_type not in EVENT_TYPES:
            raise ValueError(f"Unsupported event type: {event_type}")

        expanded = jsonld.expand(content, options={"expand_context": EVENT_CONTEXT})
        self._validate_against_shapes(expanded)

        payload = build_event_payload(event_type=event_type, content=content)
        LOGGER.debug("Sending event %s to room %s", event_type, room_id)
        await self.client.room_send(room_id, message_type="m.room.message", content=payload)

    async def share_inspection_media(
        self, room_id: str, file_path: str | Path, lat: float, lon: float, thread_root: str
    ) -> None:
        """Upload geo-verified inspection media and notify room."""

        record = self.inspection_api.upload_photo(file_path, lat=lat, lon=lon)
        payload = build_event_payload(
            event_type="inspection-media",
            content={
                "@context": EVENT_CONTEXT,
                "type": "InspectionMedia",
                "contentUrl": str(record.path),
                "lat": record.location[0],
                "lon": record.location[1],
                "metadata": record.metadata,
                "inReplyTo": thread_root,
            },
        )
        await self.client.room_send(room_id, message_type="m.room.message", content=payload)

    async def sync_forever(self) -> None:
        """Begin syncing and reacting to new messages."""

        self.client.add_event_callback(self._on_message, RoomMessageText)
        await self.client.sync_forever(timeout=30000)

    async def _on_message(self, room: MatrixRoom, event: RoomMessageText) -> None:
        if event.sender == self.client.user:
            return
        try:
            content = json.loads(event.body)
            expanded = jsonld.expand(content, options={"expand_context": EVENT_CONTEXT})
            self._validate_against_shapes(expanded)
            LOGGER.info("Validated inbound message in room %s", room.room_id)
        except Exception as exc:  # pylint: disable=broad-except
            LOGGER.warning("Failed to validate inbound message: %s", exc)

    def _validate_against_shapes(self, expanded_jsonld: Iterable[dict]) -> None:
        graph = Graph().parse(data=json.dumps(expanded_jsonld), format="json-ld")
        conforms, results_graph, results_text = validate(
            data_graph=graph,
            shacl_graph=str(self.config.shapes_file),
            inference="rdfs",
        )
        if not conforms:
            raise ValueError(results_text)

    @property
    def _server_name(self) -> str:
        if self.config.server_name:
            return self.config.server_name
        parsed = urlparse(self.config.homeserver)
        return parsed.hostname or self.config.homeserver

    @staticmethod
    def _sanitize_alias(value: str) -> str:
        """Keep Matrix room aliases predictable and server-safe."""

        return re.sub(r"[^A-Za-z0-9._-]", "-", value)


async def bootstrap_permit_room(bot: MatrixPermitBot, permit_id: str, participants: Iterable[str]) -> str:
    """Ensure a room exists and invite participants."""

    room_id = await bot.ensure_room(permit_id)
    for mxid in participants:
        try:
            await bot.client.room_invite(room_id, mxid)
        except Exception as exc:  # pylint: disable=broad-except
            LOGGER.warning("Failed to invite %s to %s: %s", mxid, room_id, exc)
    return room_id


async def push_status_update(
    bot: MatrixPermitBot, room_id: str, status: str, data: Optional[Dict[str, Any]] = None
) -> None:
    payload = {
        "@context": EVENT_CONTEXT,
        "type": "PermitStatus",
        "status": status,
    }
    if data:
        payload.update(data)
    await bot.send_event(room_id, "status-update", payload)


async def create_applicants_thread(
    bot: MatrixPermitBot, permit_id: str, applicants: Iterable[str]
) -> str:
    room_id = await bootstrap_permit_room(bot, permit_id, participants=applicants)
    await bot.send_event(
        room_id,
        "submission",
        {"@context": EVENT_CONTEXT, "type": "PermitSubmission", "permitId": permit_id},
    )
    return room_id


def run_bot_from_env() -> None:
    """Convenience entrypoint for standalone bot execution."""

    import os

    config = MatrixBotConfig(
        homeserver=os.getenv("MATRIX_HOMESERVER", "http://localhost:6167"),
        user=os.environ["MATRIX_USER"],
        password=os.environ["MATRIX_PASSWORD"],
        device_id=os.getenv("MATRIX_DEVICE_ID"),
    )
    bot = MatrixPermitBot(config)

    async def _main() -> None:
        await bot.login()
        await bot.sync_forever()

    asyncio.run(_main())


__all__ = [
    "MatrixBotConfig",
    "MatrixPermitBot",
    "bootstrap_permit_room",
    "push_status_update",
    "create_applicants_thread",
    "run_bot_from_env",
]
