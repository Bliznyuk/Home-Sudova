---
name: house-html-report-builder
description: Build source-backed House Sudova HTML reports for exterior concepts, landscape plans, lighting plans, before-after reviews, cost scopes, decision logs, and contractor packages. Use when project-output-builder or the General Contractor needs a polished local HTML deliverable. Reports must preserve fact status labels and must not invent quantities, materials, dimensions, orientation, drainage, soil, or costs.
---

# House HTML Report Builder

## Role

Create warm, restrained, source-backed HTML reports for House Sudova. This skill packages approved or clearly marked planning content; it does not create new design decisions by itself.

Adapted from `report-generator`: retained structured report sections, charts/tables, and self-contained HTML output; removed generic KPI defaults and added source/fact discipline for a private house project.

## Coordination

- Use `skills/project-manager-general-contractor` for scope, routing, dependencies, and conflicts.
- Use `skills/project-output-builder` when assembling final project packages; this skill can produce the HTML version.
- Use `skills/architecture-review` before including exterior visualizations, image prompts, facade changes, mounted elements, drainage near the house, or roof-adjacent proposals.
- Use `house-source-spec` and `architectural-source-intake` for fact tables and source evidence.
- Use `before-after-image-qa` for image comparison findings, with its limitation stated.

## Report Requirements

Every report must include:

- Title, date, report purpose, and status: concept, planning, review, or handoff.
- Protected house elements.
- Known / Observed / User-provided / Assumption / Missing fact table.
- Source list with file paths, notes, or user-provided references.
- Scope separated into must-have, should-have, nice-to-have, and later when implementation is involved.
- Risks, manual checks, contractor/professional verification items, and open questions.
- Clear exclusions: not construction drawings, not engineering approval, not electrical approval, not contractor quote.

## Visual Style

Use organic modern / warm natural minimalism:

- warm greige, off-white, muted stone, graphite-brown, muted olive, and natural wood tones;
- simple typography, generous but not wasteful spacing;
- concise tables and small diagrams;
- no glossy showroom, high-tech, futuristic, luxury-villa, or commercial marketing style;
- no decorative gradient blobs or fake hero marketing sections.

## Content Rules

- Do not create charts unless the underlying quantities are known or explicitly assumption-based.
- Do not show cost totals unless the estimator supplied quantities, assumptions, confidence, exclusions, and contingency.
- Do not place generated images beside source photos without labeling them as proposal or visualization.
- Caption every image with status: source photo, observed condition, proposal render, prompt output, or QA image.
- Keep Ukrainian climate, maintenance, freeze-thaw, snow, mud, rain, heat, and wind risks visible when relevant.

## Suggested Structure

Use only sections needed for the task:

1. Executive summary.
2. Protected geometry and source status.
3. Existing conditions.
4. Proposed concept or plan.
5. Specialist findings.
6. Diagrams or schedules.
7. Budget or scope table.
8. Risks and manual checks.
9. Open questions and next decisions.

## HTML Output Guidance

Create local HTML that can be opened directly unless the user asks for a hosted app. Prefer a self-contained file with inline CSS for reports.

Recommended location:

| Output | Location |
| --- | --- |
| Draft report | `outputs/reports/<topic>-draft.html` |
| Final report | `outputs/reports/<topic>.html` |
| Report assets | `outputs/reports/assets/` |

If source images are local, reference them by relative paths only when the report will stay in the workspace. For a portable report, copy assets into the report asset folder and keep source attribution.

## Final QA

Before delivery, check:

- No invented facts slipped into captions, tables, diagrams, or totals.
- All assumptions are labeled.
- Protected elements are listed.
- Visualizations are clearly separated from source photos.
- Manual checks and contractor/professional verification are visible.
- The report reads as a private planning package, not a sales landing page.
