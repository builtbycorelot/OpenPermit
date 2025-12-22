# OpenPermit API Specifications

This directory contains the **unified API catalog** for OpenPermit — a single source of truth integrating REST, MCP, and gRPC paradigms.

## Overview

### unified-api-catalog.yaml

**OpenAPI 3.1 specification** serving as the meta-framework for all API interfaces:

- ✅ **REST/OpenAPI endpoints** — Traditional HTTP APIs for permit management
- ✅ **JSON-LD schemas** — Semantic web integration with NIEM 6.0
- ✅ **MCP tools catalog** — LLM-discoverable tools for AI integration (via `x-mcp-tools`)
- ✅ **gRPC definitions** — High-performance RPC with embedded protobuf specs (via `x-grpc`)

## Why Unified?

**Problem:** Multiple API paradigms (REST, MCP, gRPC) require separate specs, leading to:
- Schema drift between interfaces
- Duplicated documentation
- Inconsistent behavior across protocols

**Solution:** Single OpenAPI 3.1 spec with vendor extensions for MCP and gRPC.

**Benefits:**
- **Single source of truth** — One schema, multiple protocols
- **Automatic consistency** — REST, MCP, and gRPC share same data models
- **Interoperability** — Clients can choose protocol based on needs
- **Reduced maintenance** — Update once, deploy everywhere

## Structure

```yaml
openapi: 3.1.0
info: {...}
servers: [...]
paths:
  /applications: {...}      # REST endpoints
  /permits: {...}
  /inspections: {...}
  /validate/ifc: {...}
  /nodes: {...}
  /crosswalks: {...}

components:
  schemas:
    Application: {...}      # Shared data models
    Permit: {...}
    Inspection: {...}
    ValidationResult: {...}

  x-mcp-tools:             # MCP tool catalog for LLM discovery
    - name: create_application
      description: "..."
      inputSchema: {...}
      handler:
        method: POST
        path: /applications

  x-grpc:                  # gRPC protobuf definitions
    package: openpermit.v1
    services:
      - name: ApplicationService
        methods: [...]
    messages: [...]
```

## Usage Patterns

### 1. REST API (Traditional HTTP)

**Standard OpenAPI client generation:**

```bash
# Generate TypeScript client
openapi-generator-cli generate \
  -i specs/unified-api-catalog.yaml \
  -g typescript-fetch \
  -o clients/typescript

# Generate Python client
openapi-generator-cli generate \
  -i specs/unified-api-catalog.yaml \
  -g python \
  -o clients/python
```

**Usage:**

```typescript
import { ApplicationsApi } from './clients/typescript';

const api = new ApplicationsApi();
const app = await api.createApplication({
  applicant: { name: "Jane Builder" },
  project: { name: "ADU Addition" }
});
```

### 2. MCP Tools (LLM Integration)

**The `x-mcp-tools` extension provides Claude/GPT-discoverable tools.**

**MCP server implementation:**

```typescript
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { unified-api-catalog } from "./specs/unified-api-catalog.yaml";

const server = new Server({
  name: "openpermit-mcp",
  version: "1.0.0"
}, {
  capabilities: {
    tools: {}
  }
});

// Auto-register tools from x-mcp-tools
for (const tool of catalog['x-mcp-tools']) {
  server.setRequestHandler(CallToolRequestSchema, async (request) => {
    if (request.params.name === tool.name) {
      // Map to REST endpoint via tool.handler
      const response = await fetch(`${baseURL}${tool.handler.path}`, {
        method: tool.handler.method,
        body: JSON.stringify(request.params.arguments)
      });
      return { content: [{ type: "text", text: JSON.stringify(await response.json()) }] };
    }
  });
}
```

**Claude Desktop integration:**

```json
{
  "mcpServers": {
    "openpermit": {
      "command": "node",
      "args": ["path/to/openpermit-mcp-server.js"]
    }
  }
}
```

**Usage in Claude:**

> **User:** "Create a permit application for a 1,200 sq ft ADU in Austin, TX"
>
> **Claude:** *[Uses `create_application` MCP tool with schema validation]*
>
> Application created successfully. ID: APP-2024-001234

### 3. gRPC (High-Performance RPC)

**Generate gRPC stubs from `x-grpc` definitions:**

```bash
# Extract protobuf from OpenAPI
./scripts/extract-grpc-proto.sh specs/unified-api-catalog.yaml > openpermit.proto

# Generate Go stubs
protoc --go_out=. --go-grpc_out=. openpermit.proto

# Generate Python stubs
python -m grpc_tools.protoc -I. \
  --python_out=. \
  --grpc_python_out=. \
  openpermit.proto
```

**Usage:**

```go
import pb "openpermit/v1"

client := pb.NewApplicationServiceClient(conn)
app, err := client.CreateApplication(ctx, &pb.ApplicationRequest{
    Applicant: &pb.Applicant{Name: "Jane Builder"},
    Project: &pb.Project{Name: "ADU Addition"},
})
```

### 4. JSON-LD / Semantic Web

**All schemas include JSON-LD `@context` for semantic interoperability:**

```json
{
  "@context": "https://schema.openpermit.org/v1",
  "@type": "Application",
  "@id": "https://permits.example.com/applications/APP-001234",
  "status": "submitted",
  "project": {
    "@type": "Project",
    "name": "ADU Addition"
  }
}
```

**NIEM 6.0 alignment:**

The schemas extend NIEM Justice/Infrastructure domains for federal compliance.

## API Endpoints

### Applications

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/applications` | GET | List applications |
| `/applications` | POST | Create application |
| `/applications/{id}` | GET | Get application details |
| `/applications/{id}` | PATCH | Update application |
| `/applications/{id}/submit` | POST | Submit for review |

### Permits

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/permits` | GET | List permits |
| `/permits/{id}` | GET | Get permit details |

### Inspections

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/inspections` | POST | Schedule inspection |
| `/inspections/{id}` | GET | Get inspection details |
| `/inspections/{id}/findings` | POST | Submit findings |

### Validation

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/validate/ifc` | POST | Validate IFC model against code |
| `/validate/application` | POST | Validate application data |

### Node Framework

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/nodes` | POST | Create node |
| `/nodes/{id}` | GET | Get node |
| `/nodes/{id}/validate` | POST | Validate node |
| `/crosswalks` | POST | Create crosswalk |
| `/crosswalks/{id}` | GET | Get crosswalk |

## MCP Tools Catalog

**LLM-discoverable tools via Model Context Protocol:**

| Tool | Description |
|------|-------------|
| `list_endpoints` | Meta-tool to discover available endpoints |
| `create_application` | Create permit application |
| `get_application` | Retrieve application by ID |
| `submit_application` | Submit for review |
| `list_permits` | List permits with filters |
| `get_permit` | Get permit details |
| `schedule_inspection` | Schedule building inspection |
| `get_inspection` | Get inspection results |
| `submit_inspection_findings` | Record inspection findings |
| `validate_ifc_model` | Validate IFC against building codes |
| `validate_application_data` | Validate application completeness |
| `create_node` | Create ontological node |
| `validate_node` | Validate node rules |
| `create_crosswalk` | Create standard-to-standard mapping |

## gRPC Services

**High-performance RPC services:**

- **ApplicationService** — Create, read, update, submit applications
- **PermitService** — Retrieve permit data
- **InspectionService** — Schedule and manage inspections
- **ValidationService** — IFC and application validation
- **NodeService** — Ontological node framework operations

## Schema Highlights

### Key Features

1. **JSON-LD `@context`** — All responses include semantic web context
2. **NIEM 6.0 alignment** — Federal standard compliance
3. **IFC integration** — Building models linked via `ifcGlobalId`
4. **BCF compatibility** — Review comments map to BIM Collaboration Format
5. **Versioned** — Semantic versioning for backward compatibility

### Core Models

- **Application** — Permit application with status, stakeholders, documents
- **Permit** — Issued permit with inspections, conditions, regulations
- **BuildingPermit** — Extends Permit with IFC model linkage
- **Inspection** — Schedule, findings, inspector certification
- **Finding** — Element-level inspection results linked to IFC
- **ValidationResult** — Code compliance check results
- **Node** — Ontological framework node
- **Crosswalk** — Standard-to-standard mapping

## Development Workflow

### 1. Edit Specification

```bash
# Edit unified catalog
vim specs/unified-api-catalog.yaml

# Validate OpenAPI syntax
npx @redocly/cli lint specs/unified-api-catalog.yaml
```

### 2. Generate Clients

```bash
# Generate all clients
./scripts/generate-clients.sh

# Output:
# - clients/typescript/
# - clients/python/
# - clients/go/
```

### 3. Deploy

```bash
# Build API server from spec
npm run build:api

# Deploy
npm run deploy
```

## Tooling

### Recommended Tools

- **Editor:** [Stoplight Studio](https://stoplight.io/studio) (OpenAPI visual editor)
- **Validation:** [Redocly CLI](https://redocly.com/docs/cli/)
- **Documentation:** [ReDoc](https://redocly.github.io/redoc/) or [Swagger UI](https://swagger.io/tools/swagger-ui/)
- **Mock Server:** [Prism](https://stoplight.io/open-source/prism)
- **Client Generation:** [OpenAPI Generator](https://openapi-generator.tech/)

### Scripts

```bash
# Validate spec
npm run validate:spec

# Generate documentation
npm run docs:generate

# Start mock server
npm run mock:server

# Generate all clients
npm run generate:clients

# Extract gRPC protobuf
npm run extract:grpc
```

## Architecture Principles

### 1. Schema-First Development

**Spec drives implementation, not reverse:**

```
unified-api-catalog.yaml (source of truth)
        ↓
    ┌───┴───┐
    │       │
REST API   gRPC    MCP Tools
  impl     stubs    handlers
```

### 2. Protocol Interoperability

**Same schema, multiple protocols:**

| Use Case | Protocol | Reason |
|----------|----------|--------|
| **Web/mobile apps** | REST | Wide compatibility, HTTP caching |
| **Microservices** | gRPC | High performance, streaming |
| **AI assistants** | MCP | LLM-native discovery, validation |

### 3. Semantic Interoperability

**JSON-LD enables:**
- Federal standard alignment (NIEM)
- Cross-jurisdiction data portability
- Linked open data publication (CKAN)

## Versioning Strategy

**Semantic versioning for backward compatibility:**

- **Patch (1.0.x)** — Bug fixes, clarifications (no breaking changes)
- **Minor (1.x.0)** — New optional fields, new endpoints (backward compatible)
- **Major (x.0.0)** — Breaking changes (avoided when possible)

**Version negotiation:**

```http
GET /applications
Accept: application/json; version=1.0
```

## Migration from Legacy APIs

If you have existing REST endpoints not in this spec:

1. **Add to `paths`** section
2. **Define schemas** in `components/schemas`
3. **Add MCP tool** in `x-mcp-tools` (if LLM-relevant)
4. **Add gRPC method** in `x-grpc` (if needed)
5. **Validate** with `npm run validate:spec`

**Example:**

```yaml
paths:
  /legacy/endpoint:
    get:
      summary: "..."
      # ...rest of definition

# Add corresponding MCP tool
x-mcp-tools:
  - name: legacy_action
    handler:
      method: GET
      path: /legacy/endpoint
```

## References

- [OpenAPI 3.1 Specification](https://spec.openapis.org/oas/v3.1.0)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [gRPC Protocol Buffers](https://protobuf.dev/)
- [JSON-LD 1.1](https://www.w3.org/TR/json-ld11/)
- [NIEM 6.0](https://niem.github.io/)

## Contributing

When adding new endpoints:

1. Define in `paths` with full OpenAPI schema
2. Add corresponding schema in `components/schemas`
3. If LLM-relevant, add to `x-mcp-tools`
4. If high-performance critical, add to `x-grpc`
5. Include JSON-LD `@context` for semantic interop
6. Update this README with new endpoints

## Support

- **Issues:** https://github.com/builtbycorelot/OpenPermit/issues
- **Discussions:** https://github.com/builtbycorelot/OpenPermit/discussions
- **Email:** j@corelot.net

---

**Key Insight:**

> **One spec. Three protocols. Zero drift.**

The unified API catalog eliminates schema inconsistencies by making OpenAPI 3.1 the single source of truth for REST, MCP, and gRPC interfaces.
