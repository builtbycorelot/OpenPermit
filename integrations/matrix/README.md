# Matrix integration for OpenPermit

This module wires OpenPermit workflow events into the Matrix protocol using a small bot powered by [`matrix-nio`](https://github.com/poljar/matrix-nio). Conduit is the default self-hosted homeserver target and is packaged with a ready-to-run Docker Compose file.

## Components

- `MatrixPermitBot`: joins or creates a room per permit application and publishes JSON-LD workflow events for submissions, updates, approvals, and inspections.
- `MatrixEventValidator`: enforces SHACL validation on incoming Matrix payloads using the shapes defined in `shapes.ttl`.
- `conduit/docker-compose.yml`: spins up a Conduit homeserver that Element and other Matrix clients can connect to for decentralized discussions.

## Usage

1. Start Conduit locally:
   ```bash
   docker compose -f integrations/matrix/conduit/docker-compose.yml up -d
   ```
2. Configure the bot:
   ```python
   from integrations.matrix import MatrixConfig, MatrixPermitBot

   config = MatrixConfig(
       homeserver="http://localhost:6167",
       user_id="@bot:openpermit",
       access_token="<bot access token>",
       default_participants={"@inspector:openpermit", "@reviewer:openpermit"},
   )
   bot = MatrixPermitBot(config)
   ```
3. Send events tied to permits:
   ```python
   await bot.send_permit_event(
       permit_id="PERMIT-123",
       event_type="submission",
       payload={"submissionPath": "submissions/PERMIT-123.json"},
       status="received",
       actor="permit-applicant",
   )
   ```
4. Relay geo-verified inspection media through the Remote Inspection API and into the Matrix room thread:
   ```python
   await bot.send_inspection_media(
       "PERMIT-123",
       Path("/tmp/site-photo.png"),
       lat=37.7749,
       lon=-122.4194,
       actor="@inspector:openpermit",
       thread_root="$event-for-threading",
   )
   ```

The bot will validate every outgoing and incoming event against the SHACL shapes before updating workflow submissions or ingesting inspection photos.
