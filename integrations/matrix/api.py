"""HTTP-facing integration helpers for Matrix permit collaboration."""
from __future__ import annotations

import asyncio
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Mapping

from remote_inspection.api import PhotoInspectionAPI

from .bot import (
    MatrixBotConfig,
    MatrixPermitBot,
    bootstrap_permit_room,
    push_status_update,
)
from .message_schemas import EVENT_CONTEXT


@dataclass
class PermitParticipant:
    permit_id: str
    matrix_ids: List[str]
    webhook_url: str | None = None


class MatrixPermitService:
    """Facade for OpenPermit workflows to trigger Matrix interactions."""

    def __init__(self, bot: MatrixPermitBot) -> None:
        self.bot = bot

    async def start_permit_thread(self, permit: PermitParticipant) -> str:
        room_id = await bootstrap_permit_room(
            self.bot, permit.permit_id, participants=permit.matrix_ids
        )
        await self.bot.send_event(
            room_id,
            "submission",
            {
                "@context": EVENT_CONTEXT,
                "type": "PermitSubmission",
                "permitId": permit.permit_id,
                "summary": f"Permit {permit.permit_id} submitted",
            },
        )
        return room_id

    async def notify_status(self, room_id: str, status: str, data: Mapping[str, str] | None = None) -> None:
        await push_status_update(self.bot, room_id, status=status, data=dict(data or {}))

    async def push_approval(self, room_id: str, approver: str, notes: str | None = None) -> None:
        await self.bot.send_event(
            room_id,
            "approval",
            {
                "@context": EVENT_CONTEXT,
                "type": "PermitApproval",
                "approvedBy": approver,
                "summary": notes or "Permit approved",
            },
        )

    async def share_inspection_media(
        self, room_id: str, file_path: str | Path, lat: float, lon: float, thread_root: str
    ) -> None:
        await self.bot.share_inspection_media(room_id, file_path=file_path, lat=lat, lon=lon, thread_root=thread_root)


async def initialize_service_from_env(participants: Iterable[str]) -> MatrixPermitService:
    import os

    bot_config = MatrixBotConfig(
        homeserver=os.getenv("MATRIX_HOMESERVER", "http://localhost:6167"),
        user=os.environ["MATRIX_USER"],
        password=os.environ["MATRIX_PASSWORD"],
        device_id=os.getenv("MATRIX_DEVICE_ID"),
        inspection_api=PhotoInspectionAPI(),
    )
    bot = MatrixPermitBot(bot_config)
    await bot.login()
    return MatrixPermitService(bot)


__all__ = ["MatrixPermitService", "PermitParticipant", "initialize_service_from_env"]
