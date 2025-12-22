# Fee Vocabulary

OpenPermit fee definitions must be clear, taggable, jurisdiction-mappable, and accounting-reconcilable so they can export as financial facts (XBRL mapping). This vocabulary aligns identifiers, basis rules, and linked-data context for fee items.

## Goals
- clear, taggable, jurisdiction-mappable
- accounting-reconcilable
- exportable as financial facts (XBRL mapping)

## FeeCode Examples (stable identifiers)
- `permit.base`
- `permit.plan_review`
- `inspection.initial`
- `inspection.reinspection`
- `inspection.after_hours`
- `trade.electrical.base`
- `trade.plumbing.base`
- `trade.mechanical.base`
- `fire.alarm`
- `fire.suppression`

## YAML Stub
See [`schemas/vocab/fee_vocabulary.yaml`](../../schemas/vocab/fee_vocabulary.yaml) for the machine-readable vocabulary scaffold.

## JSON-LD Context Stub
`contexts/fee.jsonld` defines linked data terms for `PermitFee`, `feeCode`, `accountCode`, `permitId`, `jurisdiction`, `amount`, `currency`, `basis`, `quantity`, `anchor`, and `ts`.
