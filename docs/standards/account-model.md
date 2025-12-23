# Standard Account Model (Permit Finance Slice)

A FeeItem is a financial fact. It must map cleanly to a standard account code for reconciliation, audit, and reporting.

## Minimal Standard Accounts (permit slice)

### Revenue
- `4300.PERMIT_REVENUE`
- `4310.PLAN_REVIEW_REVENUE`
- `4320.INSPECTION_REVENUE`
- `4330.REINSPECTION_REVENUE`
- `4340.AFTER_HOURS_REVENUE`

### Contra/Adjustments
- `4800.FEE_WAIVERS`
- `4810.FEE_REFUNDS`

## YAML Stub
See [`schemas/vocab/account_codes.yaml`](../../schemas/vocab/account_codes.yaml) for the machine-readable vocabulary scaffold.

## XBRL Note
Define FeeItem exports as “financial facts” with:
- `concept = FeeCode`
- `context = permitId + jurisdiction + period`
- `unit = USD`
- `value = amount`

(Do not build full taxonomy yet; provide stub mapping guidance.)
