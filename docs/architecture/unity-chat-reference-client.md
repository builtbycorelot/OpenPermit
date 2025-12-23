# Unity Chat is a Reference Authoring Client

OpenPermit’s mission is civic transparency and sovereign data. We therefore treat all renderers and UIs as replaceable, and all authoritative outputs as open artifacts.

Unity Chat exists as a *reference operator interface* to validate one essential capability:
**a human authority can select a building element and emit a durable, standards-native assertion.**

Unity Chat is **not**:
- the system of record
- the identity provider
- the workflow engine
- the hosting environment
- the distribution channel

Unity Chat **must always**:
- read open formats (IFC / CityGML)
- write open formats (IFC annotations + JSON-LD events)
- export to open interchange (OpenUSD and/or glTF)
- emit linked data suitable for audit (JSON-LD) and finance (XBRL mapping)

**Principle:** Chat is the UI. IFC/USD is the truth. JSON-LD is the meaning. OData is the query surface.

## Why not Matrix?
Matrix is excellent as a transport layer for conversational events, but our primary UX is not “messaging”—it is **spatially anchored assertions** bound to geometry, scope, and provenance. Matrix can carry events downstream; it is not the canonical authoring surface for spatial review.

**Matrix is a bus. Unity/WebGL is the cockpit. IFC/USD/JSON-LD is the truth.**
