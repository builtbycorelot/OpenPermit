# Provider Adapter Contract

## Adapter Role
Translate OpenPermit events (JSON-LD) into provider-specific API calls, and write back provider IDs.

## Inputs (minimum)
- `ReviewComment`
- `InspectionRequest`
- `InspectionResult`
- `FeeItem`

## Outputs (minimum)
- `providerEventId`
- `status` (accepted/rejected)
- `timestamp`
- optional `providerUrl`

## Non-goals
- No identity/auth in OpenPermit (providers keep theirs)
- No hosting requirements
- No workflow replacement
