---
name: image-prompting
description: Create House Sudova photorealistic image-generation and image-edit prompts, render briefs, night-scene prompts, landscape visualizations, before/after edits, style variants, and negative prompts while preserving exact original house geometry. Use only after architecture-review for any visualization that could alter the house; include constraints to preserve roof shape/slope, windows, doors, column rhythm, wall positions, AC unit, and main proportions.
---

# Image Prompting

## Role

Act as the visualization prompt department. Translate approved design intent into prompts that protect the real house geometry and avoid accidental fantasy architecture.

## Mandatory Prerequisite

Run `architecture-review` before generating image prompts or visualization briefs for House Sudova. The review must confirm protected elements and flag geometry, drainage, mount, AC, or facade risks.

If the design itself is not yet defined, use the relevant design department first: `exterior-house-designer`, `landscape-master-planner`, `house-lighting-designer`, `ukrainian-plants`, or `project-manager-general-contractor`.

## Use This Skill For

- Photorealistic exterior prompts, image-edit prompts, before/after visualizations, prompt packs, negative prompts, night renders, landscape previews, material tests, and style variants.
- Prompt refinement when generated images drift from the real house.
- View-specific prompt constraints for preserving windows, doors, roof, columns, AC, wall positions, and proportions.

## Inputs Needed

- Original image, exact view reference, or source photo path.
- Architecture-review notes and protected geometry list.
- Desired changes and explicit "do not change" items.
- Materials, lighting, plants, ground treatment, season, weather, time of day, and mood.
- Known orientation and sun/time constraints if daylight is important.
- Target platform if known: image edit, text-to-image, inpainting, prompt pack, or render brief.

If orientation, sun direction, season, materials, or site dimensions are unknown, ask or label the prompt assumption-based.

## Outputs to Produce

- Protected geometry list.
- Main photorealistic prompt.
- Negative prompt.
- Edit/masking instructions when image editing is intended.
- Variant prompts when useful.
- Assumptions and risk notes.
- Handoff notes for output packaging or cost/design follow-up.

## Mandatory Preservation Constraints

Include these constraints in every House Sudova prompt:

- Preserve exact house geometry.
- Preserve roof shape and slope.
- Preserve existing windows and doors: size, color, shape, and position.
- Preserve column rhythm.
- Preserve wall positions and main proportions.
- Keep the AC unit unless explicitly requested otherwise.
- Change only the requested exterior materials, lighting, landscape, planting, and ground treatment.

## Coordination Requirements

- Coordinate with `architecture-review` before prompt generation and after reviewing generated images for drift.
- Coordinate with `sun-position-analysis` when the prompt specifies daylight, shadows, season, facade heat, or time of day.
- Coordinate with `exterior-house-designer` for facade materials, colors, and style.
- Coordinate with `landscape-master-planner`, `soil-irrigation-drainage`, and `ukrainian-plants` for plausible landscape, soil, ground treatment, and plant context.
- Coordinate with `house-lighting-designer` for night prompts, 2700K ambience, fixture logic, beams, glare, and scene realism.
- Coordinate with `project-output-builder` when assembling prompt packs by view.

## Prompting Rules

- Prioritize photorealism and continuity with the provided image.
- Anchor the prompt to the original view and camera angle.
- Avoid language that implies a different house, changed roof, moved windows, new openings, luxury showroom, glass villa, futuristic facade, or invented geometry.
- Use organic modern / warm natural minimalism language.
- Prefer warm greige mineral plaster, natural wood, dark graphite-brown metal, natural stone, microcement, gravel, meadow planting, and restrained planting masses when appropriate.
- For lighting images, specify 2700K warm white and avoid cool, blue, RGB, or theatrical light.
- Use negative prompts to block geometry drift, extra windows, changed roofline, changed columns, changed doors, removed AC, warped proportions, glossy finishes, and unrealistic materials.

## Response Checklist

- Architecture review has been run or explicitly identified as required before final prompt use.
- Prompt anchors to the provided original image/view.
- Protected elements are named clearly.
- Requested changes are specific and limited.
- Negative prompt blocks geometry drift.
- Landscape and plants are suitable for Ukrainian countryside context when relevant.
- Sun/time instructions do not conflict with known orientation.
- Assumptions are visible.
