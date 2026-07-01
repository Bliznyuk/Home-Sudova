# House Sudova Codex Instructions

Use this project as a private exterior architecture, lighting, landscape, plant, visualization, and budgeting workspace for a Ukrainian countryside house.

## Non-Negotiable Rule

Never invent missing site dimensions, sun orientation, materials, soil, drainage, utilities, electrical capacity, or costs. If information is missing, ask the user or clearly mark assumptions.

## Protected House Constraints

- Preserve the real geometry of the house.
- Do not move, resize, recolor, or reshape existing windows and doors unless the user explicitly asks.
- Do not change the roof shape, roof slope, column rhythm, wall positions, or main proportions.
- Keep the AC unit unless the user explicitly asks to remove or relocate it.
- Distinguish clearly between observed existing conditions, design proposals, and assumptions.

## Design Direction

- Style: organic modern / warm natural minimalism.
- Avoid high-tech, cold showroom, glossy, overly commercial, futuristic, or luxury-villa looks.
- Prefer warm natural materials: wood, warm greige mineral plaster, dark graphite-brown metal or structural elements, natural stone, microcement, gravel, meadow planting, and restrained architectural lighting.
- Exterior lighting must be warm white 2700K, with 3000K as the absolute maximum.
- Design for Ukrainian countryside climate: freeze-thaw cycles, snow, summer heat, rain, wind, mud, dust, insects, and seasonal maintenance.
- Assume sandy or sandy-loam soil only when no soil test is available, and mark that assumption.
- Always consider sun position, shade, overheating, wind, privacy, drainage, maintenance, and contractor buildability.

## Landscape Form Language

Use a soft-geometric landscape language that supports the house's real rectilinear geometry without copying it too rigidly or fighting it with decorative curves.

- Main functional paths should be simple, calm, and aligned with real entries, the gate, carport, terrace, and service routes. Use straight or lightly offset orthogonal lines where they serve daily movement; avoid arbitrary winding paths.
- Garden destination paths may be softer: large rectangular stepping slabs through lawn or gravel joints, or one broad gentle arc when it connects a real destination such as a fire lounge, gazebo, or garden seating area. Do not create many narrow serpentine paths.
- Planting beds should use broad asymmetric drifts, soft rounded or oval edges, and large repeated masses. Avoid small scalloped borders, scattered single plants, rigid decorative patterns, and a continuous thuja-wall look unless needed for a specific technical screen.
- A fire lounge or special seating area may be circular or softly oval as the organic counterpoint to the rectangular house and terrace. Use this as one calm destination gesture, not as many competing circles.
- Plant forms should be layered: low grasses/perennials at path edges, medium shrubs for mass and privacy, and a few small trees for structure. Repeat 3-5 main plant groups in masses instead of collecting many unrelated specimens.
- Keep taller or denser plant masses away from windows, doors, AC airflow/service, downspouts, facade lights, path lights, camera views, and maintenance routes at mature size.
- Treat exact path widths, radii, bed outlines, plant quantities, and spacing as missing until confirmed from the real plan, sun orientation, soil/drainage, irrigation, lighting routes, and field layout.

## Team Operating Model

Think of the skills as departments in a design-and-build company.

- The user is the client / owner.
- `skills/project-manager-general-contractor` is the default entry point for complex or cross-discipline tasks.
- Specialist skills are departments. They provide discipline advice, then the General Contractor reconciles dependencies, sequencing, budget priority, and conflicts.
- Specialists must check dependencies with other skills when their decisions affect another discipline.
- Final answers should feel coordinated, not like separate departments arguing. If disciplines conflict, state the conflict, recommended option, reason, and what must be checked before implementation.

Use the General Contractor skill when a request involves two or more of: exterior design, architecture review, sun/shade, landscape, drainage, irrigation, soil, plant selection, lighting, electrical routing, automation, visualization, budget, phasing, or contractor sequencing.

For narrow single-discipline tasks, use the relevant specialist skill, but still respect dependencies. For example, plant selection still needs sun and soil assumptions; lighting still needs landscape and electrical routing assumptions.

## Skill Routing

- Use `skills/project-manager-general-contractor` for complex tasks, implementation roadmaps, dependency maps, contractor checklists, scope prioritization, and conflict resolution.
- Use `skills/house-project-planning` for durable planning files, progress logs, decision logs, open-question lists, and multi-session continuity. This is a support skill under the General Contractor, not a replacement coordinator.
- Use `skills/house-source-spec` before fact-dependent work to inventory known, observed, user-provided, assumed, and missing dimensions, orientation, materials, drainage, soil, utilities, protected geometry, and source evidence. Do not use fallback defaults.
- Use `skills/architectural-source-intake` to extract cautious facts from photos, plans, marked-up views, PDFs, screenshots, and contractor sketches before architecture review, visualization, diagrams, reports, or estimates.
- Use `skills/architecture-review` before changing architecture, facade rhythm, roof-adjacent elements, structural-looking elements, drainage near the house, mounted elements, or any image prompt / visualization brief that could alter the house.
- Use `skills/sun-position-analysis` before landscape planning, plant selection, shade design, terrace comfort, facade overheating decisions, daylight-sensitive visualizations, or privacy decisions linked to exposure.
- Use `skills/exterior-house-designer` for facade materials, color palettes, entry composition, terrace/canopy refinements, and warm natural exterior concepts.
- Use `skills/landscape-master-planner` for full-site zoning, circulation, privacy, hardscape, outdoor rooms, grading assumptions, maintenance access, and phasing.
- Use `skills/soil-irrigation-drainage` before finalizing planting, irrigation, drainage, grading, soil preparation, water grouping, downspout handling, or underground routes.
- Use `skills/ukrainian-plants` for plant palettes that must survive Ukrainian climate and match soil, light, water, wind, maintenance, and mature-size constraints.
- Use `skills/house-lighting-designer` for architectural and landscape lighting, fixture placement, beam logic, cable routes, transformers, junction boxes, circuits, automation zones, and 2700K ambience.
- Use `skills/image-prompting` when preparing image-generation or image-edit prompts that must preserve the original house geometry.
- Use `skills/before-after-image-qa` to compare source photos with generated or edited images after architecture review. Treat it as a support check only; it cannot prove geometry preservation by itself.
- Use `skills/site-analysis-diagrams` for Mermaid diagrams that explain dependencies, phases, missing facts, drainage logic, sun/shade scenarios, planting-lighting conflicts, or contractor sequencing. Do not create measured site plans or orientation diagrams from missing data.
- Use `skills/cost-estimator` after scope, quantities, materials, fixtures, plant counts, labor assumptions, supplier assumptions, and exclusions are known or explicitly marked.
- Use `skills/project-output-builder` to assemble final packages: concept notes, prompt packs, plant schedules, lighting schedules, cost tables, decision logs, contractor checklists, and roadmaps.
- Use `skills/house-html-report-builder` when a source-backed local HTML report is needed for concepts, reviews, schedules, cost scopes, decision logs, or contractor packages. It packages approved or clearly labeled content; it does not invent facts or replace `project-output-builder`.

## Cross-Discipline Coordination

Landscape and Lighting:

- Do not place trees or large shrubs where they will block planned facade lighting, path lighting, camera views, or service access.
- Do not place lights where future plants will cover them at mature size.
- Coordinate cable routes, sleeves, transformers, junction boxes, and fixture access before paths, lawn, irrigation, and planting are finalized.

Landscape, Soil, Irrigation, and Drainage:

- Do not finalize planting without soil, drainage, and irrigation assumptions.
- Group plants by watering needs.
- Consider sandy or sandy-loam soil only when no soil test is available, and mark it as an assumption.
- Resolve runoff, muddy circulation, downspout discharge, snowmelt, and freeze-thaw base issues before final hardscape or planting.

Lighting and Electrical:

- Plan low-voltage lighting routes before hardscape installation.
- Mark likely transformer, driver, junction box, conduit, sleeve, exterior outlet, and smart relay locations.
- Avoid designing lights that are beautiful but impossible, unsafe, intrusive, or expensive to wire.
- Keep all electrical recommendations as planning guidance until verified by a qualified electrician.

Exterior and Architecture Review:

- Do not change roof shape, slope, windows, doors, column rhythm, wall positions, or main wall geometry unless explicitly requested by the user.
- Any visual change must preserve the original building structure unless the user explicitly asks otherwise.
- Check facade penetrations, attachment methods, plinth/base details, waterproofing, gutters, snow, and drainage before recommending exterior materials or lighting mounts.

Plants and Sun Position:

- Plant selection must consider sun exposure, shade, heat, wind, snow, soil, water, privacy, and mature size.
- Do not recommend full-sun plants for shaded areas or moisture-loving plants for dry sandy zones without irrigation and soil-improvement assumptions.
- Do not block windows, doors, AC airflow/service, paths, planned lights, or key views with mature plant growth.

Cost and Design:

- Every design proposal should be separated into: must-have, should-have, nice-to-have, and later.
- Hidden infrastructure and irreversible work come before visible finishes.
- Estimates must show assumptions, confidence, exclusions, contingency, and whether prices are current or planning-level.

## Conflict Resolution

When two departments conflict, the General Contractor resolves the conflict before answering.

Priority order:

1. Safety and buildability.
2. Preservation of real house geometry.
3. Climate and durability for Ukraine.
4. Water, drainage, soil, and maintenance practicality.
5. Budget realism.
6. Aesthetics.

The final answer should say:

- what the conflict was;
- which option is recommended;
- why;
- what should be checked before implementation.

Do not expose internal disagreement as chaos. Return one coordinated recommendation with tradeoffs.

## Visualization Rule

Before generating image prompts or visualization briefs, run `skills/architecture-review`.

The `skills/image-prompting` output must include preservation constraints:

- preserve exact house geometry;
- preserve roof shape and slope;
- preserve windows and doors: size, color, shape, and position;
- preserve column rhythm;
- preserve wall positions;
- keep the AC unit unless explicitly requested otherwise;
- change only the requested exterior materials, lighting, landscape, and ground treatment.

If orientation, season, sunlight direction, or material facts are missing, ask the user or clearly label the prompt as assumption-based.

Use `skills/before-after-image-qa` after generated or edited images exist, but do not treat it as proof that protected geometry is preserved. It can flag visible drift and support prompt iteration; architecture review and source verification remain required.

## Combined Workflow

1. Read available source materials first: photos, plans, existing project notes, marked-up views, decision logs, and previous prompts in this workspace.
2. Use `house-source-spec` and, when source images/plans are involved, `architectural-source-intake` to mark facts as Known / Observed / User-provided / Assumption / Missing.
3. Confirm missing essentials: dimensions, north orientation, facade orientation, sun exposure, soil, drainage, utilities, electrical capacity, irrigation source, budget, timeline, and maintenance level.
4. For complex work, start with `project-manager-general-contractor` to classify scope, route departments, and sequence decisions.
5. Use `house-project-planning` for durable planning when work spans phases, sessions, disciplines, or contractor packages.
6. Run `architecture-review` for any proposal that touches the house envelope, roof-adjacent details, columns, openings, drainage near the house, mounted elements, built elements, or visualizations.
7. Run `sun-position-analysis` before committing to shade, planting, terrace comfort, privacy screening, facade heat-control ideas, or daylight-sensitive visuals.
8. Develop exterior and landscape concepts separately, then reconcile them into one coherent site plan.
9. Resolve soil, irrigation, drainage, grading, and underground route assumptions before final hardscape and planting.
10. Select Ukrainian-climate plants after exposure, soil, water, wind, and maintenance are known or explicitly assumed.
11. Design lighting after architecture and landscape zones are stable enough to avoid rework; coordinate electrical and low-voltage routes before hardscape.
12. Build image prompts only after protected geometry and design changes are explicit.
13. Use `before-after-image-qa` to review generated images for visible drift, then route issues back to architecture review and image prompting.
14. Estimate costs with clear quantities, assumptions, confidence levels, exclusions, and contingency.
15. Package outputs with open questions, next decisions, and protected constraints visible; use `house-html-report-builder` only for source-backed HTML reports.

## Routing Examples

Exterior visualization:

1. `architecture-review`: confirm protected geometry, AC, windows, doors, roof, columns, wall positions, drainage, and mount risks.
2. `sun-position-analysis`: check orientation and plausible daylight if the view depends on sun/shade.
3. `exterior-house-designer`: define materials, colors, and organic modern direction if not already defined.
4. `landscape-master-planner` and `house-lighting-designer`: add ground treatment, planting masses, or 2700K lighting only when requested.
5. `image-prompting`: create prompt with mandatory preservation constraints.
6. `project-output-builder`: package prompt variants and decision notes if needed.

Landscape + lighting plan:

1. `project-manager-general-contractor`: define scope, zones, and sequencing.
2. `sun-position-analysis`: map exposure, terrace comfort, privacy, and heat.
3. `landscape-master-planner`: plan zones, paths, outdoor rooms, screens, and hardscape.
4. `soil-irrigation-drainage`: resolve soil, runoff, water groups, trenching, and irrigation assumptions.
5. `ukrainian-plants`: select plants that fit exposure, water, soil, and mature-size constraints.
6. `house-lighting-designer`: place fixtures, beams, routes, transformers, and control zones without conflicting with plants or paths.
7. `cost-estimator`: price phases after quantities are known or marked.
8. `project-output-builder`: assemble the plan, schedules, and next checks.

Plant selection:

1. `sun-position-analysis`: confirm or scenario-map exposure.
2. `soil-irrigation-drainage`: confirm soil, drainage, irrigation, watering zones, and soil improvement assumptions.
3. `landscape-master-planner`: confirm the planting role and mature-space envelope.
4. `ukrainian-plants`: produce the plant palette and avoid list.
5. `house-lighting-designer`: check that mature planting will not cover planned fixtures where relevant.
6. `cost-estimator`: estimate plant, soil, mulch, irrigation, and labor costs if requested.

Cost estimate:

1. `project-manager-general-contractor`: define scope and must-have / should-have / nice-to-have / later categories.
2. Pull quantities and specs from `landscape-master-planner`, `soil-irrigation-drainage`, `ukrainian-plants`, `house-lighting-designer`, and `exterior-house-designer`.
3. `cost-estimator`: create low/base/high planning estimate with assumptions, exclusions, and confidence.
4. `project-output-builder`: create a budget summary or purchase-phase document if needed.

Full implementation roadmap:

1. `project-manager-general-contractor`: lead the whole process.
2. Read sources and decision logs.
3. Route architecture, sun, landscape, soil/irrigation/drainage, plants, lighting/electrical, cost, and output packaging in sequence.
4. Resolve conflicts using the priority order.
5. Deliver phased work packages, contractor checklists, dependencies, open questions, and budget priorities.

## Output Discipline

- Use concise tables for plants, lighting, materials, costs, phases, dependencies, and contractor tasks.
- Include a short assumptions section whenever facts are incomplete.
- List protected elements in every visual or architectural proposal.
- Separate observed existing conditions, assumptions, proposals, and contractor verification items.
- Prefer phased recommendations over one large vague plan.
- Separate every proposal into must-have, should-have, nice-to-have, and later when budget or implementation is involved.
- Do not present rough concepts as construction drawings, engineering approval, electrical approval, legal advice, or contractor quotes.
