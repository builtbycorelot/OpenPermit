"""Matrix bot bridging permit events and chat threads."""

from __future__ import annotations

import asyncio
import json
import logging
from pathlib import Path
from typing import Any, Dict, Iterable, Optional

from nio import AsyncClient, JoinError, LoginError, RoomMessage, UnknownEvent
from pyshacl import validate
from rdflib import Graph

from remote_inspection import PhotoInspectionAPI
from workflow import submission

from .config import MatrixConfig
from .messages import EVENT_TYPES, build_jsonld_event

logger = logging.getLogger(__name__)


class MatrixEventValidator:
    """Validate JSON-LD payloads against the provided SHACL shapes."""

    def __init__(self, shapes_path: Path) -> None:
        self.shapes_path = Path(shapes_path)
        self.shapes_graph = Graph().parse(self.shapes_path)

    def validate(self, event: Dict[str, Any]) -> None:
        data_graph = Graph().parse(data=json.dumps(event), format="json-ld")
        conforms, _, results_text = validate(
            data_graph,
            shacl_graph=self.shapes_graph,
            inference="rdfs",
            abort_on_first=False,
        )
        if not conforms:
            raise ValueError(f"Matrix event failed SHACL validation: {results_text}")


class MatrixPermitBot:
    """Matrix client that mirrors permit workflow events into chat threads."""

    def __init__(
        self,
        config: MatrixConfig,
        inspection_api: Optional[PhotoInspectionAPI] = None,
    ) -> None:
        self.config = config
        self.client = AsyncClient(
            homeserver=config.homeserver,
            user=config.user_id,
            device_id=config.device_id,
        )
        self.client.access_token = config.access_token
        self.validator = MatrixEventValidator(config.shacl_shapes_path)
        self.inspection_api = inspection_api or PhotoInspectionAPI()

    async def login(self) -> None:
        """Perform a login if an access token is not pre-configured."""
        if self.client.access_token:
            return
        resp = await self.client.login(password=None)  # type: ignore[arg-type]
        if isinstance(resp, LoginError):
            raise RuntimeError(f"Matrix login failed: {resp.message}")

    async def ensure_room(self, permit_id: str, participants: Iterable[str] | None = None) -> str:
        """Join or create a room dedicated to a permit application."""
        alias = self.config.alias_for_permit(permit_id)
        alias_local = alias.split(":")[0].lstrip("#")
        try:
            resp = await self.client.join(alias)
            if isinstance(resp, JoinError):
                raise RuntimeError(resp.message)
            return resp.room_id
        except Exception:
            logger.info("Creating room for permit %s", permit_id)

        creation = await self.client.room_create(
            name=f"Permit {permit_id}",
            is_direct=False,
            preset="private_chat",
            alias=alias_local,
            invite=list(self.config.participants(participants)),
        )
        if hasattr(creation, "room_id"):
            return creation.room_id
        raise RuntimeError(f"Unable to create room for permit {permit_id}: {creation}")

    async def send_permit_event(
        self,
        permit_id: str,
        event_type: str,
        payload: Dict[str, Any],
        *,
        status: str | None = None,
        actor: str | None = None,
        participants: Iterable[str] | None = None,
        thread_root: str | None = None,
    ) -> Dict[str, Any]:
        """Validate and transmit an OpenPermit workflow event."""
        room_id = await self.ensure_room(permit_id, participants)
        event = build_jsonld_event(
            permit_id,
            event_type,
            payload,
            status=status,
            actor=actor,
            thread_root=thread_root,
        )
        self.validator.validate(event)
        await self.client.room_send(
            room_id=room_id,
            message_type="org.openpermit.event",
            content=event,
            ignore_unverified_devices=True,
        )
        return event

    async def send_inspection_media(
        self,
        permit_id: str,
        file_path: Path,
        lat: float,
        lon: float,
        *,
        actor: str | None = None,
        thread_root: str | None = None,
    ) -> Dict[str, Any]:
        """Upload geo-verified media and broadcast metadata to the permit room."""
        record = self.inspection_api.upload_photo(file_path, lat, lon)
        payload = {
            "mediaPath": str(record.path),
            "location": {"lat": lat, "lon": lon},
            "analysis": record.metadata,
        }
        return await self.send_permit_event(
            permit_id,
            "inspection-media",
            payload,
            actor=actor,
            thread_root=thread_root,
        )

    async def handle_event(self, room, event) -> None:
        """Dispatch incoming events to workflow and inspection hooks."""
        if isinstance(event, UnknownEvent):
            content = event.source.get("content", {})
            msg_type = event.source.get("type")
        elif isinstance(event, RoomMessage):
            content = getattr(event, "source", {}).get("content", {})
            msg_type = getattr(event, "source", {}).get("type")
        else:
            return

        if msg_type != "org.openpermit.event":
            return

        try:
            self.validator.validate(content)
        except ValueError as exc:
            logger.warning("Rejecting invalid Matrix content: %s", exc)
            return

        self._handle_workflow_side_effects(content)

    def _handle_workflow_side_effects(self, content: Dict[str, Any]) -> None:
        """Bridge Matrix content into local workflow systems."""
        permit_id = content.get("permitId")
        status = content.get("status")
        payload = content.get("payload", {})
        if permit_id and status and payload.get("submissionPath"):
            submission.update_submission(
                payload["submissionPath"],
                {"status": status, "data": payload},
                content.get("actor", "matrix"),
            )

        if content.get("@type") == EVENT_TYPES.get("inspection-media"):
            location = payload.get("location", {})
            lat = location.get("lat") or location.get("latitude")
            lon = location.get("lon") or location.get("longitude")
            media_path = payload.get("mediaPath")
            if media_path and lat is not None and lon is not None:
                try:
                    self.inspection_api.upload_photo(Path(media_path), float(lat), float(lon))
                except Exception as exc:  # pragma: no cover - defensive logging
                    logger.warning("Failed to ingest inspection media: %s", exc)

    async def run_forever(self, timeout_ms: int = 30000) -> None:
        """Start syncing and listening for permit events."""
        self.client.add_event_callback(self.handle_event, (UnknownEvent, RoomMessage))
        while True:
            await self.client.sync(timeout=timeout_ms)
            await asyncio.sleep(0)
