# Public Site Inventory & Astro Card Catalog ToC

This document captures the public-facing page inventory for the C3 housing–focused OpenPermit standard (with W3C extensions) and a ready-to-ingest Card Catalog table of contents for Astro. Every page listed here should render meaningful HTML on first response (no JS-dependent metadata), expose stable canonicals, and ship the structured data called out in the earlier SEO/AEO guidance.

## Source of truth
- **Card catalog data:** `docs/astro-card-catalog.json` — one entry per public URL with title, summary, canonical, schema types, section, tags, and ordering.
- **Goal:** Import this JSON into the Astro Card Catalog component to generate the table of contents and route cards without relying on client-side discovery.

## Coverage checklist
The JSON inventory includes:
1) Overview: `/`, `/demo`, `/app`
2) Models: `/models`, `/models/fzk-haus`, `/models/institute`, `/models/road`, `/models/bridge`
3) Standards: `/standards/ifc`, `/standards/web-annotation`, `/standards/verifiable-credentials`
4) Answers (AEO-first): `/answers/ifc-permitting`, `/answers/ifc-georeference`, `/answers/web-annotation-plan-review`, `/answers/product-bindings-traceability`, `/answers/ontology-validators-ci`
5) Docs: `/docs`, `/docs/governance`, `/docs/conformance`, `/docs/api`, `/docs/validators`
6) Support: `/faq`

## How to load into Astro
```ts
// Example: src/content/catalog.ts (Astro)
import catalog from '../docs/astro-card-catalog.json';

const sectionOrder = {
  'Overview': 1,
  'Models': 2,
  'Standards': 3,
  'Answers': 4,
  'Support': 5,
  'Docs': 6
};

export const toc = catalog
  .sort((a, b) => {
    const sectionDiff = sectionOrder[a.section] - sectionOrder[b.section];
    return sectionDiff !== 0 ? sectionDiff : a.order - b.order;
  });
```

```astro
--- // Example: ToC page
import { toc } from '../content/catalog';
---
<section aria-labelledby="catalog-heading">
  <h1 id="catalog-heading">OpenPermit C3 Housing Standard</h1>
  {toc.map((card) => (
    <Card
      title={card.title}
      href={card.slug}
      description={card.summary}
      badge={card.section}
      tags={card.tags}
    />
  ))}
</section>
```

## QA expectations
- Every entry in `docs/astro-card-catalog.json` should appear in the rendered Card Catalog with the same slug, title, and summary.
- Canonicals must match the slugs defined in the catalog (no JS rewrites).
- Breadcrumbs and structured data should be present in the raw HTML for each page using the schema types listed per entry.
- PWA/WebGL pages (`/app`, `/demo`) must serve an HTML synopsis before hydration; the catalog entry provides the text for the pre-hydration payload.

## Notes for future updates
- Add new public pages by appending objects to `docs/astro-card-catalog.json`; keep `section` and `order` consistent to avoid navigation drift.
- If a page is deprecated, set its `status` to `"deprecated"` and remove it from the Astro import map to prevent stale cards from rendering.
- Keep summaries short (≤160 chars) to align with meta descriptions and card copy.
