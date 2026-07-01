---
name: before-after-image-qa
description: Support QA workflow for comparing House Sudova before/after exterior renders, image edits, prompt outputs, and visualization variants against source photos. Use to flag geometry drift, changed windows or doors, altered roof, missing AC, material mismatches, and prompt/render issues. This is a support check only and cannot prove geometry preservation by itself.
---

# Before After Image QA

## Role

Compare a source image and an edited/generated image for House Sudova visualization quality. This skill supports, but never replaces, `skills/architecture-review`.

Adapted from `image-compare`: retained before/after comparison and difference review; removed visual-regression pass/fail assumptions and added House Sudova geometry-preservation checks.

## Mandatory Prerequisite

Run or reference `skills/architecture-review` before using this skill for any image that could alter the house. If architecture review has not happened, state that the QA is preliminary.

## Hard Limit

Pixel matching, overlays, and visual inspection can flag problems, but they cannot prove real geometry preservation. Always report this limitation.

## QA Checklist

Compare these items first:

| Item | Check |
| --- | --- |
| Roof | Shape, slope, overhangs, ridges, gutters, and proportions unchanged unless approved |
| Windows | Size, color, shape, position, count, rhythm, and trim relationship unchanged unless approved |
| Doors | Size, color, shape, position, and visual relationship unchanged unless approved |
| Columns | Rhythm, spacing, thickness, and structural appearance preserved |
| Walls | Main planes, corners, massing, and proportions preserved |
| AC | Present, not relocated or visually erased unless explicitly requested |
| Ground/grade | No invented steps, retaining walls, slopes, or drainage corrections unless specified |
| Materials | Proposed materials match approved design notes and are not glossy/cold/showroom-like |
| Lighting | Warm white 2700K, 3000K maximum, no blue/RGB/theatrical light unless explicitly requested |
| Landscape | Plants and hardscape do not block doors, windows, AC airflow, service access, or lights |

## Optional Technical Checks

Use existing local tools if already available; do not install dependencies just for QA unless the user asks.

- Confirm both images have comparable crop, aspect ratio, and viewpoint.
- Generate an overlay or diff only as a visual aid.
- Inspect the full image manually after any pixel-level check.
- If crops or camera angles differ, rely on protected-element review rather than mismatch percentages.

## Output Format

Use a concise table:

| Area | Finding | Severity | Status | Action |
| --- | --- | --- | --- | --- |
| Roof | Roofline appears taller in after image | High | Observed | Reject or regenerate |

Severity:

- `High`: protected geometry drift, missing AC, changed roof, moved openings, unsafe visual implication.
- `Medium`: material, lighting, scale, drainage, or landscape plausibility issue.
- `Low`: polish, color cast, crop, season, small artifact.

## Verdicts

- `Reject`: geometry drift or protected element changed.
- `Revise`: concept useful but needs prompt/render correction.
- `Preliminary pass`: no obvious drift, but architecture review or source verification still required.

Always include: "This QA check supports but does not prove geometry preservation."
