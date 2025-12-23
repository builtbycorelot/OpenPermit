# Dynamic Documentation from Canonical Schemas

This blueprint describes how to serve documentation directly from the canonical sources of truth—ontology index (YAML), JSON-LD contexts, OpenAPI specs, and MCP endpoint definitions—so that reference docs stay consistent across UI, adapters, and APIs.

## Sources of Truth
- **Ontology index**: `ontology/index.yaml` (classes, properties, relationships, namespaces)
- **JSON-LD contexts**: `contexts/*.jsonld` (ontology, fee, inspection, nodes)
- **API definitions**: OpenAPI/Swagger files (to be added/updated in `openapi/` or `integrations/`)
- **Adapter/MCP endpoints**: Structured endpoint specs for provider adapters (future `mcp/endpoints.yaml` or similar)

## Pipeline Goals
1. **Single namespace map** — emitted from `ontology/index.yaml` and reused by contexts and schemas.
2. **Generated reference pages** — static site pages (Markdown/HTML) built from the ontology and OpenAPI/MCP specs.
3. **Consistency checks** — CI tasks that fail when a term exists in one source but not the others.
4. **Embeddable snippets** — JSON-LD examples and OData/OpenAPI snippets generated alongside docs.

## Proposed Build Steps
1. Parse `ontology/index.yaml` → emit:
   - JSON-LD context fragments (validated against `contexts/ontology.jsonld`)
   - Markdown tables for classes/properties/relationships
2. Parse OpenAPI specs → emit:
   - Endpoint summaries, request/response schemas
   - Example payloads aligned to ontology classes
3. Parse MCP endpoint specs → emit:
   - Endpoint list, inputs/outputs, capability matrix
4. Cross-check:
   - Ensure every class/property in generated docs maps to a namespace in `ontology/index.yaml`
   - Ensure JSON-LD contexts reference defined classes/properties
5. Publish:
   - Generate static docs into `docs/.generated/` (or `site/`) consumed by the docs site

## Tooling Options
- **Node/TS**: Use `yaml` + `jsonld` packages to transform `ontology/index.yaml` and contexts.
- **Python**: Use `ruamel.yaml`/`pyld` for the same transformations in CI.
- **OpenAPI**: `swagger-cli` / `openapi-typescript` for validation and client examples.
- **MCP**: Define a simple YAML schema for endpoints, then render via Jinja/Handlebars.

## Integration Points
- Add CI job: `npm run docs:generate` or `python scripts/gen_docs.py` to rebuild generated docs and fail on drift.
- Link generated outputs from `docs/README.md` once the pipeline is wired.
- Keep human-written guidance (like this file) minimal—most reference tables should be generated.

## Next Steps
- Add OpenAPI/MCP source files to the repo (e.g., `openapi/openpermit.yaml`, `mcp/endpoints.yaml`).
- Create a small generator script to turn `ontology/index.yaml` into:
  - Updated `contexts/ontology.jsonld`
  - Markdown tables under `docs/.generated/ontology.md`
- Wire a CI check to validate that contexts and schemas align with the ontology index.
