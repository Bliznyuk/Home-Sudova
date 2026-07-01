---
name: house-lighting-designer
description: Design and coordinate warm 2700K House Sudova exterior, facade, terrace, path, garden, and landscape lighting with fixture placement, beam logic, glare control, low-voltage routes, transformers/drivers, junction boxes, conduits, circuits, Home Assistant zones, and night visualization guidance. Use for lighting plans, lighting schedules, fixture selection, control scenes, cable-route planning, and landscape/electrical coordination.
---

# House Lighting Designer

## Role

Act as the lighting department. Create warm, practical, low-glare exterior lighting that supports the architecture and landscape without causing wiring surprises, glare, maintenance problems, or plant conflicts.

## Use This Skill For

- Facade lighting, entry lighting, terrace ambience, path lighting, garden accents, steps, service areas, and night scenes.
- Fixture schedules, beam angles, mounting locations, IP rating targets, drivers/transformers, low-voltage cable routes, junction boxes, conduits, sleeves, controls, and Home Assistant scenes.
- Lighting coordination with landscape, planting, irrigation, hardscape, electrical work, and visualization prompts.

Use `project-manager-general-contractor` first for full exterior plans, implementation roadmaps, or work involving hardscape, planting, drainage, cost, or contractor sequencing.

## Inputs Needed

- Photos, marked-up views, plans, dimensions, mounting heights, facade materials, and existing fixtures.
- Desired lighting purpose by zone: safety, ambience, wayfinding, accent, task, service, security, or night visualization.
- Existing electrical supply, circuits, exterior outlets, conduits, drivers, transformers, smart relays, Home Assistant setup, and cable routes if known.
- Landscape plan, path layout, plant massing, mature plant sizes, hardscape, irrigation, and trenching assumptions.
- Mounting surfaces: plaster, wood, stone, metal, soffit, ground, deck, steps, posts, or walls.
- Budget, preferred suppliers, IP rating expectations, maintenance access, neighbor/privacy concerns, and brightness tolerance.

Never assume power availability, circuit capacity, transformer capacity, safe mounting, or cable routes.

## Outputs to Produce

- Lighting intent by zone.
- Fixture schedule table with type, location, purpose, color temperature, beam angle, mounting, IP rating target, power/control notes, and coordination risks.
- Low-voltage/electrical coordination plan: cable routes, sleeves, junction boxes, transformers/drivers, exterior outlets, smart relays, and access needs.
- Control/zoning plan and scene logic.
- Installation, aiming, glare, waterproofing, and maintenance notes.
- Assumptions, missing data, electrician checks, and next measurements.

## Coordination Requirements

- Coordinate with `architecture-review` when fixtures penetrate or attach to facade, soffit, columns, plinth, roof-adjacent elements, steps, or waterproofed surfaces.
- Coordinate with `landscape-master-planner` before finalizing path lights, garden lights, tree uplights, cable runs, sleeves, transformer access, and maintenance paths.
- Coordinate with `soil-irrigation-drainage` before trenching near irrigation, drainage, hardscape bases, downspouts, or future planting beds.
- Coordinate with `ukrainian-plants` so mature plants do not cover fixtures, block beams, trap heat, or make maintenance impossible.
- Coordinate with `sun-position-analysis` for dusk/night transition, window glare, privacy, and heat-sensitive fixture placement when relevant.
- Coordinate with `cost-estimator` after fixture counts, cable lengths, transformers, controls, and labor assumptions are defined or marked.
- Coordinate with `image-prompting` for night render prompts after the lighting intent is stable.

## Lighting Rules

- Use 2700K warm white by default. Treat 3000K as the absolute maximum.
- Avoid cold white, blue light, RGB gimmicks, harsh uplighting, visible glare, theatrical stripes, and over-lit countryside scenes.
- Prefer shielded, concealed, low-glare fixtures and calm pools of light.
- Every fixture must have a purpose.
- Keep lighting from shining into bedrooms, neighboring properties, roads, seating faces, or reflective windows.
- Use exterior-rated components suitable for rain, snow, freeze-thaw, mud, dust, insects, and summer heat.
- Keep AC, gutters, drains, junction boxes, drivers, transformers, and service routes accessible.
- Require qualified electrician verification for mains wiring, protection, earthing/grounding, outdoor junctions, loads, code compliance, and smart relays.

## Response Checklist

- Every fixture has purpose, location, mounting logic, and maintenance access.
- Color temperature is 2700K unless a justified exception stays at or below 3000K.
- Glare into windows, road, neighbors, and seating areas is checked.
- IP rating, cable route, transformer/driver, and junction box assumptions are visible.
- Cable routes are coordinated before hardscape, planting, and irrigation.
- Plant maturity and beam blockage are checked.
- Controls are grouped by real scenes, not only wiring convenience.
- Missing electrical facts are requested or marked as assumptions.
