# Prescriptive Project Verification

Many projects can be approved rapidly when they follow well-defined rules. OpenPermit supports "e-check" style validation that compares a submission to codified requirements, allowing municipalities to deliver faster, more predictable approvals.

## How it works
1. **Structured inputs.** Submissions use the [standardized vocabulary](standardized_vocabulary.md) so every data point is addressable.
2. **Rule libraries.** Local ordinances, ICC references, and policy directives are expressed as machine-readable checks.
3. **Automated evaluation.** Validation engines run those checks against permit payloads or IFC models before a human ever opens the file.
4. **Transparent outcomes.** Submitters receive pass/fail results with human-readable explanations and links to governing codes.

## Standards & tooling
- [IFC Approval Workflow](ifc_approval.md) documents the BIM validation process.
- [Legal Standards Mapping](legal_standards_mapping.md) aligns regulations with data structures.
- [Code Validity Testing](code_validity_testing.md) ensures new policy language can be translated into automation-friendly logic.

## Benefits
- Speeds up reviews for prescriptive housing and energy retrofit projects.
- Reduces subjective decisions, increasing equity across applicants.
- Gives staff more time for complex, discretionary reviews.

## Contributing rules
- Share reusable rule sets via GitHub issues or pull requests.
- Tag new validations with jurisdiction, code reference, and effective date.
- Coordinate with policy teams to keep logic aligned with enacted ordinances.
