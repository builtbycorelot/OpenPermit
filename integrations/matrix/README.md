# Matrix + Conduit integration for OpenPermit

This module wires OpenPermit workflows to Matrix using the [`matrix-nio`](https://github.com/poljar/matrix-nio) SDK and a Conduit homeserver. Each permit application can have its own Matrix room with structured JSON-LD messages and SHACL validation.

## Components
- `bot.py`: asyncio bot that joins/creates rooms, validates JSON-LD payloads with SHACL, and surfaces Remote Inspection media threads.
- `api.py`: thin service layer suitable for hooking into existing OpenPermit APIs.
- `message_schemas.py`: shared JSON-LD context and helper for event payloads.
- `shapes/permit.shacl.ttl`: SHACL shapes for submissions, statuses, and inspection media.
- `conduit/docker-compose.yml`: ready-to-run Conduit configuration for local testing.

## Running Conduit locally
```
cd integrations/matrix/conduit
docker compose up -d
```
The homeserver will be reachable at `http://localhost:6167`. Create a service account (e.g., `@openpermit:localhost`) and set the credentials as environment variables when running the bot.

## Running the bot
```
export MATRIX_USER=@openpermit:localhost
export MATRIX_PASSWORD=supersecret
export MATRIX_HOMESERVER=http://localhost:6167
python -m integrations.matrix.bot
```

## Using the service layer
```
import asyncio
from integrations.matrix.api import MatrixPermitService, PermitParticipant, initialize_service_from_env

async def main():
    service = await initialize_service_from_env(["@applicant:localhost"])
    room_id = await service.start_permit_thread(PermitParticipant(
        permit_id="ABC-123",
        matrix_ids=["@applicant:localhost", "@inspector:localhost"],
    ))
    await service.notify_status(room_id, "submitted")

asyncio.run(main())
```
