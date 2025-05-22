# Badge Maintenance

This guide explains the badges displayed in the project README and how they are kept up to date.

## Security Policy
The security badge links to [`SECURITY.md`](../SECURITY.md), which outlines our FISMA and FedRAMP guidance. The badge is generated with [shields.io](https://shields.io):

```markdown
[![Security Policy](https://img.shields.io/badge/security-policy-blue.svg)](../SECURITY.md)
```

Updating the policy file automatically updates the badge because it is a simple link.

## Documentation
The documentation badge points users to the [`docs/`](../docs/) folder (or hosted docs if available):

```markdown
[![Docs](https://img.shields.io/badge/docs-online-blue.svg)](../docs/)
```

Keep this badge current if the documentation is moved or published to another location.

## Coverage
To generate a coverage report, run tests with [`coverage`](https://coverage.readthedocs.io/):

```bash
coverage run -m pytest
coverage xml
```

CI workflows can upload the results to a service like Codecov or Coveralls, which then provides a dynamic badge URL. Until such a service is configured, we use a static placeholder badge:

[![Coverage](https://img.shields.io/badge/coverage-unknown-lightgrey.svg)](docs/badges.md#coverage)

Update the badge link once automated coverage reporting is enabled.
