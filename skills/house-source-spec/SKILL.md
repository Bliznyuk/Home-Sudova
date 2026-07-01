---
name: house-source-spec
description: Source-of-truth specification workflow for House Sudova facts, dimensions, materials, orientation, utilities, drainage, soil, protected geometry, and missing information. Use before spatial planning, exterior design, image prompts, diagrams, reports, estimates, or any task that depends on project facts. This adapts building-spec behavior but disables all fallback defaults.
---

# House Source Spec

## Role

Build and maintain a factual source register for House Sudova. This skill does not design anything. It identifies what is known, observed, user-provided, assumed, or missing so other skills do not accidentally invent site facts.

Adapted from `building-spec`: retained the idea of checking project-specific specifications first; removed all fallback dimensions, room defaults, code defaults, and auto-generation behavior.

## Non-Negotiables

- Never invent dimensions, orientation, materials, drainage, soil, utilities, electrical capacity, irrigation, costs, or supplier data.
- Never fill missing values with generic residential defaults.
- Preserve the real house geometry and protected elements.
- Keep the AC unit unless the user explicitly asks otherwise.
- Mark every extracted or inferred value as `Known`, `Observed`, `User-provided`, `Assumption`, or `Missing`.
- Escalate cross-discipline implications to `skills/project-manager-general-contractor`.

## Source Search Order

Read available sources before producing or updating a spec:

1. `AGENTS.md` and local skill rules.
2. Existing project notes, decision logs, and planning files.
3. Source photos, marked-up views, plans, screenshots, and PDFs.
4. Material, lighting, landscape, cost, supplier, or contractor notes in the workspace.
5. User messages in the current thread.

If a value appears in multiple sources and conflicts, do not reconcile silently. Show the conflict and ask the General Contractor to resolve it.

## Fact Register Format

Use a concise table:

| Topic | Value | Status | Source | Confidence | Needed For | Check |
| --- | --- | --- | --- | --- | --- | --- |
| North orientation | Missing | Missing | Not found | Low | Sun, shade, diagrams | Ask user or survey |
| Existing windows | Visible in source photo | Observed | `path/to/photo.jpg` | Medium | Visualization QA | Verify against plan |

Status meanings:

| Status | Use When |
| --- | --- |
| `Known` | Verified by measurement, approved plan, or reliable project file |
| `Observed` | Visible in source material but not measured |
| `User-provided` | Stated by the user or named project note |
| `Assumption` | Provisional and explicitly stated as uncertain |
| `Missing` | Needed but unavailable |

## Protected Geometry Register

Always track these elements:

- Roof shape and slope.
- Existing windows: size, color, shape, position, rhythm.
- Existing doors: size, color, shape, position.
- Column rhythm and structural-looking supports.
- Wall positions, massing, and main proportions.
- AC unit location, airflow, condensate path, and service access.
- Known plinth, gutters, downspouts, drainage paths, and grade relationships.

If any protected element is not visible or documented, mark it `Missing`; do not assume it.

## Workflow

1. Identify the task and which facts it depends on.
2. Search existing project sources.
3. Extract facts into the status table.
4. Mark conflicts, gaps, and verification needs.
5. Route implications to the correct specialist skill.
6. Hand a clean known/missing fact list to the General Contractor.

## Disallowed Fallbacks

Do not use generic defaults for:

- ceiling or wall heights;
- window or door sizes;
- site boundaries;
- facade orientation;
- north arrow;
- soil type;
- drainage behavior;
- electrical capacity;
- material build-ups;
- supplier prices or labor rates.

If a rough scenario is useful, label it as `Assumption` and keep it separate from `Known` facts.
