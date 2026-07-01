# House Sudova Open Questions

Date: 2026-06-30  
Purpose: keep missing facts visible so future design, lighting, landscape, visualization, and budgeting work does not invent them.

Related working checklists:

- `planning/orientation-survey-intake.md` - north orientation, CAD/survey, map/compass intake.
- `planning/field-measurement-checklist.md` - facade, canopy, terrace, steps, AC, drainage, and electrical field-measurement list.

## Highest Priority

| Question | Why it matters | Owner / contractor action |
| --- | --- | --- |
| What is true north / facade orientation? | Needed for sun, shade, terrace comfort, planting, privacy, heat, and daylight prompts. | Share map/compass screenshot or plan with north arrow. |
| Is there an original survey/CAD file for the plot? | Current sources show polygon boundaries and a Figma/frame-size conflict. | Upload/export original survey, CAD, or official plan if available. |
| Which dimensions should be field-measured first: front facade, canopy, terrace, entry steps, terrace step, gate/wicket? | Needed before ordering LED profiles, cladding, pavers, or making a cost estimate. | Use `planning/field-measurement-checklist.md`; measure with laser/roulette and record actual values. |
| Where do downspouts discharge now, and where does water go after rain/snowmelt? | Drainage must come before gravel, paths, planting, and lighting trenches. | Observe after rain or ask contractor to map slopes/discharge. |
| What is the electrical panel capacity, exterior circuits, protection, and available routes? | Figma has lighting points, but not verified safe wiring/capacity. | Electrician to inspect panel, RCD/diff protection, conduit routes, and HA compatibility. |
| What clearance/service envelope does the AC unit require? | Screens, plants, lights, and cabinets near canopy can block service/airflow. | Confirm model/manual or ask AC technician. |

## Design / Scope Decisions

| Question | Why it matters | Owner action |
| --- | --- | --- |
| Are `Materials/References/*.jpg` approved as mood only, or should any single image become the primary approved reference? | Some references conflict with 2700K and geometry preservation. | Mark favorite files and what exactly you like in each: lighting, materials, planting, or overall mood. |
| Should the terrace have a very subtle soffit/cornice line, or only downlights + step + wall wash? | Figma includes terrace neon layers, but project rules avoid terrace LED frames. | Choose restrained option after architecture/lighting review. |
| Should AC be left visible, softly screened, or integrated into a ventilated technical zone? | Affects canopy screen, planting, and lighting. | Decide desired visual treatment, keeping service access. |
| What is the budget/phasing preference? | Helps separate must-have infrastructure from nice-to-have visuals. | Provide rough ceiling or phase priorities. |
| What maintenance level is acceptable for planting and lighting? | Determines plant palette, irrigation, gravel, mulch, fixture access. | Choose low / medium / high maintenance tolerance. |

## Specialist Checks Needed

| Area | Missing / needs verification | Route |
| --- | --- | --- |
| Architecture | Waterproofing, plinth, soffit build-up, facade penetrations, AC access, roof-adjacent LED mounting | `skills/architecture-review` |
| Sun/shade | Orientation, seasonal exposure, overheating, terrace comfort, plant exposure | `skills/sun-position-analysis` |
| Drainage/soil | Downspouts, muddy routes, soil, grading, trench conflicts, irrigation | `skills/soil-irrigation-drainage` |
| Landscape | Paths, planting masses, mature size, service access, privacy, phasing | `skills/landscape-master-planner` |
| Plants | Ukrainian climate palette, sun/soil/water/mature-size fit | `skills/ukrainian-plants` after sun/soil checks |
| Lighting | Final fixture count, 2700K specs, beam angles, glare, routes, transformers, HA zones | `skills/house-lighting-designer` |
| Cost | Planning estimate only after quantities/specs/exclusions are stable | `skills/cost-estimator` |
