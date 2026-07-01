# North / CAD / Survey Intake

Date: 2026-07-01  
Purpose: confirm north orientation, facade orientation, and the best available measured site source before final sun/shade, planting, lighting-route, visualization, or purchase decisions.

This is a coordination checklist, not a survey, CAD drawing, legal boundary plan, or sun study.

## Current Status

| Item | Status | Evidence checked | What this means |
| --- | --- | --- | --- |
| North orientation | Missing | No reliable north arrow found in reviewed plan photos, Figma intake, or searchable project docs | Do not finalize sun/shade, plant exposure, facade heat, privacy screens, or daylight image prompts. |
| Facade orientation | Missing | Photos show real facade relationships, but not compass direction | Use only descriptive zone names: front entry, canopy side, terrace side, back yard, service side. |
| Original CAD / survey file | Missing in workspace | Local search found no `.dwg`, `.dxf`, `.ifc`, `.skp`, `.rvt`, `.pdf`, `.pln`, `.step`, or `.stp` files | Current Figma and photo-plan dimensions remain planning evidence, not construction survey data. |
| Photo GPS / compass direction | Missing from available local metadata | `sips` exposed image size, camera, and dates only for checked photos; no usable GPS/heading data | Do not infer north from photo metadata. |
| Site boundary shape | Known from plan/Figma images, not CAD-verified | Figma boundary, `Materials/Plans/site-boundary-dimensions-sketch_IMG_1731.jpg`, `site-plan-utilities-and-access_IMG_1733.jpg`, `site-plan-house-position_M500_IMG_1736.jpg`, `marked-measured-site-plan.jpg` | Treat as a polygon, not a simple rectangle, until survey/CAD confirms it. |
| Road / entry side | Observed | Plan/photo context and `вулиця Передмістя` label in plan materials | Useful for naming zones, not enough for north. |

## What To Provide If Available

| Best source | Why it helps | Acceptable format |
| --- | --- | --- |
| Original survey / geodesy plan with north arrow | Best source for boundary, orientation, setbacks, utilities, and contractor coordination | PDF, DWG, DXF, scan/photo if clear |
| CAD export from architect/surveyor | Best working base for accurate overlays and quantities | DWG/DXF/PDF export |
| Cadastral or official plot plan | Helps reconcile boundary shape and dimensions | PDF, screenshot, scan/photo |
| Satellite/map screenshot with visible north arrow | Fastest practical orientation check | Google Maps / Apple Maps screenshot, not cropped so north arrow is visible |
| Compass screenshots from site | Useful when no survey is available | iPhone Compass screenshots/photos with the measured view direction |

## Fast Field Method For North Orientation

Use this only to establish planning orientation. It does not replace survey data.

| Step | Action | Record |
| --- | --- | --- |
| 1 | Stand at the front door, looking outward toward the yard/gate. | Compass azimuth in degrees, screenshot/photo. |
| 2 | Stand under the canopy, looking along the long canopy line toward the back/service end. | Compass azimuth in degrees, screenshot/photo. |
| 3 | Stand on the terrace, looking outward toward the garden. | Compass azimuth in degrees, screenshot/photo. |
| 4 | Stand in the back yard looking back at the terrace facade. | Compass azimuth in degrees, screenshot/photo. |
| 5 | Mark a simple north arrow on a printed plan or screenshot of the Figma/site plan. | Photo of the marked plan. |

Recommended app setup:

- Keep the phone away from metal gates, cars, columns, electrical cabinets, and power tools while measuring.
- Wait a few seconds for the compass to settle.
- Take two readings from the same point if the value jumps.
- Record the phone direction in plain language, for example: "standing at front door, looking to gate".

## Orientation Record Sheet

| ID | Position | Looking toward | Azimuth | Source photo/screenshot | Confidence | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| N-01 | Front door | Yard / gate |  |  |  |  |
| N-02 | Canopy | Along canopy |  |  |  |  |
| N-03 | Terrace | Garden |  |  |  |  |
| N-04 | Back yard | Terrace facade |  |  |  |  |
| N-05 | Marked plan | North arrow on plan |  |  |  |  |

## Guardrails Until North Is Confirmed

- Use zone names instead of cardinal directions.
- Do not label plant areas as full sun / part shade / shade except as scenarios.
- Do not make final shade-tree, privacy-screen, or overheating decisions.
- Do not specify sun angle, exact shadows, or seasonal daylight in visualization prompts.
- Keep lighting decisions independent from invented sun direction; lighting remains 2700K and low-glare by project rule.
- Keep drainage, electrical, and field dimensions as separate checks; north orientation does not solve them.

## Next Decision

Choose one source path before final sun/plant/visualization work:

| Option | Recommended when | Reliability |
| --- | --- | --- |
| Survey/CAD first | Owner can get files from architect/surveyor | Highest |
| Map screenshot + field compass | CAD is not available now but planning must continue | Medium for planning |
| Scenario-only planning | No orientation data yet | Low; use only for early concepts |
