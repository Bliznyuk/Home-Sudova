---
name: architectural-source-intake
description: Intake workflow for House Sudova architectural source material such as photos, plans, marked-up views, PDFs, screenshots, and contractor sketches. Use to extract visible conditions, protected geometry, dimensions only when explicitly shown, missing facts, and verification needs. This adapts architectural-drawing-parser behavior for Codex without US code defaults or invented measurements.
---

# Architectural Source Intake

## Role

Read source material and turn it into a cautious, traceable fact inventory. This skill supports architecture review, exterior design, diagrams, reports, image prompts, and cost scoping. It does not approve design changes.

Adapted from `architectural-drawing-parser`: retained structured extraction from drawings/photos; removed IBC/IRC assumptions, automatic compliance fields, estimated room dimensions, and generic building-code defaults.

## Mandatory Limits

- Do not infer hidden structure, dimensions, orientation, materials, drainage, or soil from appearance alone.
- Do not estimate dimensions from perspective photos unless a verified scale reference is provided; even then label the result as `Assumption` or `Observed` with low confidence.
- Do not apply US building-code categories or compliance checks.
- Do not treat OCR, vision extraction, or plan-reading guesses as verified.
- Preserve and list protected house geometry.
- Run `skills/architecture-review` before using extracted material for facade changes, exterior visualization, image prompts, mounted elements, drainage near the house, or roof-adjacent work.

## Input Types

| Source | Extract |
| --- | --- |
| Photo | Visible geometry, materials if visually clear, AC, openings, grade hints, vegetation, shadows |
| Marked-up view | User intent, requested zones, explicit notes, dimensions if written |
| Plan/PDF | Written dimensions, north arrows, labels, boundaries, notes, scale markings |
| Contractor sketch | Proposed scope, assumptions, buildability questions |
| Supplier/material note | Product names, specs, prices if present, missing compatibility checks |

## Extraction Table

Use this format:

| Item | Value | Status | Source | Confidence | Notes / Verification |
| --- | --- | --- | --- | --- | --- |
| Roof slope | Visible, unchanged in source photo | Observed | `photo.jpg` | Medium | Not measured |
| Window dimensions | Missing | Missing | Not found | Low | Need plan or measurement |

Allowed statuses: `Known`, `Observed`, `User-provided`, `Assumption`, `Missing`.

## Protected Geometry Checklist

Record whether each is visible, known, or missing:

- Roof shape and slope.
- Existing windows and doors.
- Column rhythm.
- Wall positions and main proportions.
- AC unit and service clearance.
- Plinth/base relationship.
- Gutters, downspouts, splash zones, and grade next to the house.

## Workflow

1. Identify the source file, date if known, view, and reliability.
2. Describe only what is visible or written.
3. Extract explicit dimensions only when written or measured in the source.
4. Mark unclear facts as `Missing`; mark tentative interpretations as `Assumption`.
5. Build a protected geometry list for downstream skills.
6. Flag design, drainage, material, or structure questions for `architecture-review`.
7. Pass the fact inventory to `house-source-spec` if it should become part of the source register.

## Output Requirements

- Source list with paths or descriptions.
- Fact table with status labels.
- Protected geometry list.
- Missing facts and owner questions.
- Risk notes for geometry drift, water, snow, freeze-thaw, mounting, or AC access.
- Recommended next skill routing.

Never present source intake as construction drawings, structural approval, code compliance, or contractor verification.
