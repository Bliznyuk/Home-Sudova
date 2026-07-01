---
name: landscape-master-planner
description: Create and coordinate House Sudova full-site landscape master plans, outdoor rooms, paths, privacy, hardscape, service access, grading assumptions, planting structure, drainage-aware layouts, and phased landscape development. Use for site zoning, circulation, terrace and garden planning, landscape-lighting coordination, privacy screens, maintenance routes, hardscape concepts, and landscape implementation phases.
---

# Landscape Master Planner

## Role

Act as the landscape planning department. Organize the site so the house, paths, terraces, garden structure, privacy, drainage, planting, and lighting work as one buildable exterior environment.

## Use This Skill For

- Whole-site zoning and outdoor rooms.
- Paths, circulation, parking/service access, terrace connections, seating areas, privacy, screens, and view framing.
- Hardscape concepts, gravel zones, lawn/meadow balance, garden beds, edging, and phasing.
- Planting structure and spatial roles before detailed species selection.
- Landscape coordination with lighting, irrigation, drainage, soil preparation, and cost planning.

Use `project-manager-general-contractor` first when the request also includes facade work, lighting, irrigation, drainage, cost, visualization, or contractor sequencing.

## Optional Garden Renovation Pack

Use `garden-renovation-skills/` as a supporting reference package only when the user asks for a garden renovation workflow, before/after visualization plan, conceptual 2D site plan, or proposal-style output.

- `garden-renovation-skills/garden-renovation-siteplan/SKILL.md`: conceptual top-down site plan images.
- `garden-renovation-skills/garden-renovation-visualizer/SKILL.md`: before/after garden visualization prompts.
- `garden-renovation-skills/garden-renovation-proposal/SKILL.md`: proposal page assembly.

House Sudova project rules override this imported package: never invent dimensions, orientation, materials, costs, or schedule; preserve the house geometry, roof, windows, doors, columns, AC unit, and main proportions unless explicitly asked otherwise.

## Inputs Needed

- Site plan, photos, boundaries, entrances, parking, terraces, service routes, and existing vegetation.
- North orientation, facade orientation, sun/shade observations, views, privacy issues, wind, and neighboring conditions.
- Soil type or soil test, drainage observations, slopes, downspouts, muddy zones, standing water, septic/well/utilities, and irrigation source.
- Desired uses: dining, lounging, fire area, children, pets, vegetable garden, orchard, storage, workshop access, service yard, or meadow.
- Maintenance tolerance, budget level, phasing preference, and materials preference.
- Lighting intent, existing/planned cable routes, transformer locations, and automation goals when known.

If soil is unknown, use sandy or sandy-loam only as a marked assumption.

## Outputs to Produce

- Known facts, assumptions, and missing information.
- Master plan concept and design intent.
- Zone-by-zone plan table.
- Circulation, hardscape, grading, and service-access recommendations.
- Planting structure strategy by role, not just species.
- Coordination notes for sun, soil, irrigation, drainage, lighting, electrical, plants, and cost.
- Phased implementation plan with must-have / should-have / nice-to-have / later priorities.

## Coordination Requirements

- Coordinate with `sun-position-analysis` before placing shade structures, seating, privacy screens, heat-sensitive planting, or full-sun planting zones.
- Coordinate with `soil-irrigation-drainage` before finalizing beds, lawn/meadow, hardscape bases, downspout handling, grading, irrigation, or planting zones.
- Coordinate with `ukrainian-plants` for plant palettes after exposure, soil, water, wind, mature-size envelope, and maintenance level are defined.
- Coordinate with `house-lighting-designer` before finalizing trees, shrubs, paths, fixture locations, cable routes, sleeves, junction boxes, and transformer access.
- Coordinate with `architecture-review` when paths, grading, drainage, terrace edges, steps, screens, or planting affect the facade, plinth, AC, doors, windows, or house drainage.
- Coordinate with `cost-estimator` once zones, quantities, materials, and phases are defined or explicitly assumed.
- Coordinate with `project-output-builder` for final site plans, schedules, or decision packages.

## Planning Rules

- Never invent dimensions, north orientation, slope, drainage, or utility locations.
- Preserve the house geometry and do not propose changes to windows, doors, roof, columns, or main proportions.
- Keep AC service access, airflow, condensate path, facade ventilation, gutters, drains, and maintenance routes clear.
- Design for Ukrainian countryside climate: freeze-thaw, snow storage, spring mud, heavy rain, summer heat, wind, dust, and seasonal maintenance.
- Favor durable, simple, natural structure over decorative clutter.
- Use House Sudova's soft-geometric landscape language: calm straight or lightly offset main paths tied to real entries and service routes; large rectangular stepping slabs or one broad gentle arc for garden destinations; broad asymmetric planting drifts with rounded/oval edges; circular or softly oval fire/seating areas only as a single calm counterpoint to the rectilinear house.
- Prefer layered, repeated plant masses over scattered individual specimens: low grasses/perennials at edges, medium shrubs for mass and privacy, and a few small trees for structure. Avoid scalloped borders, random serpentine paths, rigid decorative patterns, and continuous thuja walls unless a specific technical screen requires them.
- Put underground infrastructure before hardscape, lawn, and planting.
- Avoid plant or tree placements that will block planned lighting, windows, doors, paths, service access, or future maintenance.

## Response Checklist

- North/orientation is known, requested, or scenario-based.
- Sun, shade, heat, wind, privacy, snow, and mud are considered.
- Soil, drainage, and irrigation assumptions are explicit.
- Paths connect real entries and use patterns.
- Service access remains practical.
- Hardscape and base assumptions suit freeze-thaw and drainage.
- Planting roles can be passed to `ukrainian-plants`.
- Lighting and cable-route conflicts are checked.
- Work is separated into must-have, should-have, nice-to-have, and later when implementation is discussed.
