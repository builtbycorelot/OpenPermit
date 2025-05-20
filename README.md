# 🏛️ OpenPermit — Ultimately Efficient Permitting
> *Distilled for simplicity, interoperability & speed.*

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![CI](https://github.com/builtbycorelot/OpenPermit/actions/workflows/ci.yml/badge.svg)](./.github/workflows/ci.yml)
[Public demo](https://builtbycorelot.github.io/OpenPermit)

## Table of Contents
- [Overview](#overview)
- [Quick-start](#quick-start)
- [Architecture](#architecture)
- [Stakeholders & How to Engage](#stakeholders--how-to-engage)
- [Contributing](#contributing)
- [Links](#links)

## Overview
OpenPermit is an open-source data layer and tool-kit that modernises the construction-permit process.
It provides **JSON-LD workflows**, **IFC mappings**, and **validators** so applicants & agencies can speak the same language.

## Quick-start
```bash
git clone https://github.com/builtbycorelot/OpenPermit.git
cd OpenPermit
pip install -r requirements-dev.txt
pytest && python workflow/validate_workflow.py
```

## Architecture
See [mermaid/architecture.mmd](mermaid/architecture.mmd) for a high-level overview.
Example workflow data is under [workflow/workflow.jsonld](workflow/workflow.jsonld).

## Stakeholders & How to Engage

| Who | Why it matters | First steps |
| --- | -------------- | ----------- |
| Homeowners / public | Transparent status & fewer surprises | Try the demo site |
| Builders, Architects | Submit once, track everywhere | Review `workflow/workflow.jsonld` |
| Agencies & Authorities | Less data entry, instant cross-checks | Run the validator; see docs/legal-mapping.md |
| Developers | Help us extend the ontology & tools | See CONTRIBUTING.md |

## Contributing
We welcome issues and pull requests—start by reading the style guide in [CONTRIBUTING.md](CONTRIBUTING.md).

## Links
- Docs & standards – [docs/](docs/)
- Full reference list – [docs/references.md](docs/references.md)
- Public site – https://builtbycorelot.github.io/OpenPermit
