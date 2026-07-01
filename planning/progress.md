# House Sudova Progress Log

## 2026-07-01 - House-Only Exterior Brief

Work completed:

- Created `Exterior_Lighting_Project/01_Architectural_Zones/00_House_Exterior_Brief.md` for the current architecture/facade pass without lighting.
- Recorded owner-provided clarification:
  - use the references for house appearance/material mood;
  - stairs/podiums from both sides must be explicit on the Figma plan;
  - the terrace wall with two doors is clad in wood;
  - the shorter/return terrace wall remains in the facade color.
- Updated the main entry and terrace decision logs with the stair/Figma and terrace-wall clarifications.
- Updated `planning/source-register.md` with the 2026-07-01 house-only owner clarification.
- Created `Exterior_Lighting_Project/04_House_Exterior_Visualization_Prompts_No_Lighting.md` with detailed ChatGPT prompt pack for:
  - main entry facade;
  - terrace side with two doors;
  - canopy/carport side;
  - service/technical side;
  - wide rear/garden-side view.

Current conclusion:

- The house-only direction is now separated from lighting/electrical documents.
- Figma still needs visible plan markers/labels for the stair requirement.
- If "stairs from both sides" means additional side stairs beyond the main entry and terrace side, owner markup is needed before drawing new geometry.

## 2026-07-01 - Canopy Neon Segmentation Resolution

Work completed:

- Resolved the N2 / L2 canopy neon segmentation mismatch:
  - Figma source length: 12.645 m;
  - coordination segmentation: 3 x ~4.215 m;
  - rounded planning notation allowed: 3 x ~4.22 m.
- Corrected the old `3 x ~3.95 m` note in the canopy brief.
- Updated the power schedule, BOM planning note, source register, and field-measurement checklist.

Current conclusion:

- The canopy neon segmentation no longer blocks lighting-document cleanup.
- This is still not a purchase/cut instruction: field length, product cut interval, voltage drop, feed points, junction access, and electrician routing must be verified before ordering or cutting.

## 2026-07-01 - Dimension Variance Resolution

Work completed:

- Reclassified the small dimension discrepancies as coordination variances instead of active blocking conflicts:
  - main house long facade: use 12.720 m for coordination; 12.74 m red markup is a +20 mm field-check variance;
  - terrace slab envelope: use 6.30 x 3.05 m for coordination; Figma 3.040 m is a 10 mm model variance; 3.0 m markup is rounded shorthand.
- Updated `planning/source-register.md` and `planning/field-measurement-checklist.md`.

Current conclusion:

- These two items no longer block concept, layout coordination, or lighting-document cleanup.
- They still require field measurement before exact material cuts, LED/profile ordering, cladding, tile/wood, or cost quantities.

## 2026-07-01 - Orientation And Field Measurement Package

Work completed:

- Re-checked the workspace for original CAD/survey-type files:
  - no `.dwg`, `.dxf`, `.ifc`, `.skp`, `.rvt`, `.pdf`, `.pln`, `.step`, or `.stp` files were found locally.
- Re-checked searchable project text for north/orientation/CAD/survey clues:
  - no reliable north arrow or facade orientation source was found.
- Checked available local photo metadata for representative raw/site-plan photos:
  - metadata exposed image size, camera, software, and dates;
  - no usable GPS or compass heading was exposed by the local `sips` check.
- Created the next-step source intake and measurement docs:
  - `planning/orientation-survey-intake.md`;
  - `planning/field-measurement-checklist.md`.

Current conclusion:

- North orientation remains `Missing`.
- Original CAD/survey remains `Missing in workspace`.
- Figma and plan-photo dimensions remain planning values until field-measured.
- Detailed lighting docs, purchase quantities, final plant exposure, and cost estimates should wait for orientation/survey and critical field measurements.

## 2026-06-30 - Source Inventory Start

Work completed:

- Read project instructions and local department skills for source/spec, architecture intake, architecture review, exterior design, lighting, project planning, and output packaging.
- Inventoried workspace structure:
  - `Materials/` raw photos, plans, references, annotated views.
  - `Exterior_Lighting_Project/` existing lighting/design package.
  - Local `skills/` departments.
- Read existing lighting/design docs:
  - global README, design concept, electrical/HA, power schedule;
  - main entry, canopy, terrace briefs and decision logs;
  - landscape lighting placeholder;
  - equipment/BOM/estimate placeholders;
  - visualization prompts and status matrix.
- Inspected Figma node `8:154` through the Figma connector:
  - confirmed named frame `Ділянка + будинок, натуральні розміри`;
  - extracted house, canopy, terrace, steps, lighting lines, lighting object counts, gate/wicket, technical structure, 220V markers;
  - flagged conflicts around site frame/boundary dimensions and exact facade/terrace lengths.
- Visually inspected plan/drawing images:
  - `Materials/Plans/marked-measured-site-plan.jpg`;
  - `site-boundary-dimensions-sketch_IMG_1731.jpg`, `site-plan-utilities-and-access_IMG_1733.jpg`, `site-plan-house-position_M500_IMG_1736.jpg`, `house-floor-plan_M100_IMG_1737.jpg`.
- Visually inspected representative raw photos for:
  - front entry facade;
  - canopy/carport and visible AC;
  - terrace and green wall;
  - back yard;
  - service side / downspouts / utility storage.
- Visually inspected `Materials/References` and separated usable mood from conflicts:
  - keep warm greige, wood, dark metal, low-glare layered blue-hour mood;
  - reject literal 3000K specs, full roof-outline LED, LED skeletons, geometry drift, changed windows/doors.

Outputs created:

- `planning/source-register.md`
- `planning/open-questions.md`
- `planning/progress.md`
- `planning/task-plan.md`
- Cross-link from `Exterior_Lighting_Project/00_README.md` to `planning/source-register.md`

Important conflicts found / later resolved:

- Site dimension conflict: Figma frame vs Figma boundary vector vs old README/site plan.
- House length: 12.72 m in Figma/drawings vs 12.74 m in `marked-measured-site-plan.jpg`; resolved on 2026-07-01 as coordination value 12.720 m plus field-check variance.
- Terrace depth: 3.04 m in Figma vs 3.05 m / 3.0 m in plan/markup; resolved on 2026-07-01 as coordination envelope 6.30 x 3.05 m plus field-check variance.
- Canopy neon segmentation: 12.645 m Figma length conflicted with one document saying 3 x ~3.95 m; resolved on 2026-07-01 as 3 x ~4.215 m planning segmentation.
- References repeatedly show 3000K and continuous roof/beam LED effects, conflicting with 2700K and no LED-skeleton rules.
- Figma contains many lighting objects that are not yet a final lighting schedule.

Next recommended work:

1. Confirm north orientation and source survey/CAD if available.
2. Field-measure critical facade/canopy/terrace/step dimensions.
3. Run architecture review before updating visualization prompts or construction-facing details.
4. Run soil/drainage and sun-position analysis before final landscape/plant/lighting routes.
5. Update detailed existing `Exterior_Lighting_Project` docs only after owner confirms whether `planning/source-register.md` should become the active source of truth.
