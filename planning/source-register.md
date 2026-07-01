# House Sudova Source Register

Date: 2026-07-01  
Audience: owner, designer, electrician, landscape/lighting contractor, future Codex sessions  
Purpose: factual source inventory and conflict check. This is not a construction drawing, electrical approval, drainage design, or contractor quote.

## Non-Negotiables

- Preserve the real house geometry.
- Do not move, resize, recolor, or reshape existing windows and doors unless explicitly approved.
- Do not change roof shape, roof slope, column rhythm, wall positions, or main proportions.
- Keep the AC unit and maintain airflow/service access unless explicitly approved otherwise.
- Exterior lighting default: warm white 2700K. 3000K is the absolute maximum by project rule, but current design direction should stay at 2700K or warmer.
- Missing dimensions, orientation, soil, drainage, utilities, electrical capacity, irrigation, and costs stay marked as missing until verified.

## Source Types

| Source group | Files / link | Status | Use |
| --- | --- | --- | --- |
| Project rules | `AGENTS.md`, local `skills/*/SKILL.md` | Known | Governs routing, protected geometry, climate, lighting temperature, conflict resolution |
| Figma plan | `https://www.figma.com/design/rWwIJm3D91FwbsvIgNcoQL/Untitled?node-id=8-154&t=X7MHLIydjbh2PJxe-1` | Known for drawn objects and dimensions in the file; not field-verified | Planning geometry, lighting objects, rough electrical point inventory |
| Plan/drawing photos | `Materials/Plans/site-boundary-dimensions-sketch_IMG_1731.jpg`, `site-plan-utilities-and-access_IMG_1733.jpg`, `site-plan-house-position_M500_IMG_1736.jpg`, `house-floor-plan_M100_IMG_1737.jpg`, `marked-measured-site-plan.jpg` | Known/Observed from images | Site outline, house/floor dimensions, well/septic/gate labels, floor plan areas |
| Raw site photos | `Materials/*.jpg` | Observed | Real exterior conditions, protected geometry, AC, windows/doors, drainage clues, clutter/service constraints |
| Annotated site photos | `Materials/Annotated/*.jpg`, `Exterior_Lighting_Project/00_Annotated_Viewpoints/*.jpg` | Observed derivative | Viewpoint navigation only; not primary geometry source |
| Existing project docs | `Exterior_Lighting_Project/**/*.md` | Mixed: prior decisions, drafts, estimates, prompts | Lighting/material concept, decisions, BOM drafts, visualization prompts |
| Reference images | `Materials/References/*.jpg` | User-provided mood/reference | Style and lighting mood only; not geometry source |
| Orientation / survey intake | `planning/orientation-survey-intake.md` | Working checklist; currently documents missing north/CAD status | Next owner/contractor intake for north, survey, map, and compass evidence |
| Field-measurement checklist | `planning/field-measurement-checklist.md` | Working checklist; not yet filled with field values | Facade, canopy, terrace, stairs, AC, drainage, and electrical measurement capture before detailed docs/purchases |

## Figma Node 8:154 Intake

Figma node name: `Ділянка + будинок, натуральні розміри`  
Extracted by read-only Figma inspection on 2026-06-30.

| Item | Value | Status | Source | Confidence | Notes / Check |
| --- | ---: | --- | --- | --- | --- |
| Figma frame size | 25.250 x 44.090 m | Known from Figma | Node `8:154` | Medium | Conflicts with boundary vector / old README height. Do not treat as final cadastral rectangle. |
| Boundary vector | approx. 25.250 x 44.446 m | Known from Figma object | Node `3:56` inside `8:154` | Medium | Looks like site boundary object. Needs survey/CAD confirmation. |
| Main house footprint | 12.720 x 11.850 m | Known from Figma | Node `9:1025` | High for Figma | Coordination value: use 12.720 m. The 12.74 red markup is treated as a +20 mm field-check variance, not an active design conflict. |
| House group including roof/adjacent objects | 17.260 x 14.039 m | Known from Figma | Node `9:1030` | Medium | Includes house-adjacent elements, not just wall footprint. |
| Canopy / carport | 3.540 x 11.850 m | Known from Figma | Node `1:27` | High for planning | Matches existing docs. Verify on site before paving/lighting. |
| Terrace | 6.300 x 3.040 m | Known from Figma | Node `1:28` | High for planning | Figma source value. Coordination envelope for planning is 6.30 x 3.05 m; the 10 mm depth difference is a model/rounding variance. |
| Terrace step 1 | 6.283 x 0.595 m | Known from Figma | Node `8:109` | Medium | Figma has two nearly overlapping terrace-step nodes. |
| Terrace step 2 | 6.283 x 0.600 m | Known from Figma | Node `10:1038` | Medium | Use as planning orientation only; field level controls final riser/tread. |
| Entry step 1 | 8.438 x 0.896 m | Known from Figma | Node `2:38` | Medium | Related to front step LED length. |
| Entry step 2 | 7.838 x 0.600 m | Known from Figma | Node `2:32` | Medium | Check with final step concept. |
| Entry ground-level step / podium | 9.116 x 0.300 m | Known from Figma | Node `10:1034` | Medium | Existing docs use this as entry zone width. |
| Wooden columns | 6 columns, 130 x 130 mm | Known from Figma, observed in photos | Nodes named `Деревяна колона` | High for count, medium for exact field size | Preserve rhythm. Do not move in visualizations. |
| Canopy ceiling lights | 10 planned `Потолочний світильник навіс 220В` | Known from Figma | Count summary | Medium | Planning objects only; final type/wiring not verified. |
| Terrace ceiling lights | 4 planned `Потолочний світильник тераса 220В` | Known from Figma | Count summary | Medium | Planning objects only. Existing docs prefer dimmable 24V or verified 230V. |
| Ground lights | 12 planned `Грунтовий світильник 24В` | Known from Figma | Count summary | Low/medium | Candidate layout, not final landscape lighting plan. |
| Plant uplights | 28 planned `Грунтовий світильник на рослини 24В` | Known from Figma | Count summary | Low/medium | Count may over-light site if copied literally. Coordinate with plant maturity and glare. |
| Light poles | 20 planned `Ліхтарний стовп_220В` | Known from Figma | Count summary | Low/medium | Potentially too many for current warm minimal direction; needs lighting review. |
| New 220V points | 4 planned `Нова точка 220В` | Known from Figma | Count summary | Medium | Electrical capacity, routing, protection, and circuiting missing. |
| Existing 220V point | 1 `Існуєче живлення 220В` | Known from Figma | Node `24:1328` | Medium | Need electrician/site verification. |
| Electrical cabinet / panel marker | `Щитова 220В`, approx. 0.194 x 0.389 m | Known from Figma | Node `9:1021` | Medium | Does not prove capacity. |
| Gate | approx. 4.164 m wide object | Known from Figma | Node `9:1032` | Medium | Figma object rotation/height means do not overread exact geometry. |
| Wicket | approx. 1.470 m wide object | Known from Figma | Node `9:1033` | Medium | Verify on site for lighting/cable decisions. |
| Technical structure | 1.500 x 8.749 m | Known from Figma | Node `9:1027` | Medium | Must preserve service function/access. |

## Figma Lighting Line Intake

| Figma layer | Extracted dimension | Status | Use | Check |
| --- | ---: | --- | --- | --- |
| `Гнучкий неон ВХ 24В` | 12.720 m | Known from Figma | Main/front roofline candidate | Must stop at house wall, not continue over canopy. |
| `Гнучкий неон ВХ степенька 24В` at entry | 8.438 m | Known from Figma | Entry step LED candidate | Verify exact step build-up and cut length. |
| `Гнучкий неон ВХ степенька 24В` at terrace | 6.283 m | Known from Figma | Terrace step LED candidate | Verify final terrace step after level survey. |
| `Гнучкий неон Задній двір 24В` | 6.524 m | Known from Figma | Side/back facade line candidate | Keep separate from terrace lighting; avoid LED frame effect. |
| `Гнучкий неон Тераса 1 24В` | 6.183 m | Known from Figma | Terrace-zone line candidate | Needs architecture/lighting review to avoid full perimeter lighting. |
| `Гнучкий неон Тераса 2 24В` | 3.035 m | Known from Figma | Terrace-zone line candidate | Same caution as above. |
| `Гнучкий неон Навіс 2 24В` | 12.645 m | Known from Figma | Canopy outer-beam line candidate | Segmentation resolved for coordination: 3 x ~4.215 m, rounded to 3 x ~4.22 m. Final cut depends on product and field measurement. |
| `Гнучкий неон біля споруди` | 11.979 m | Known from Figma | Side/technical-zone candidate | Not developed in existing docs; needs purpose, glare, and wiring review. |

## Plan and Drawing Intake

| Item | Value | Status | Source | Confidence | Notes / Check |
| --- | ---: | --- | --- | --- | --- |
| Location text | Sudova Vyshnia, Yavoriv district, Lviv region | Known from drawing title | `Materials/Plans/house-floor-plan_M100_IMG_1737.jpg` | Medium | Do not publish/share casually; private project context. |
| Building type | `будинку садибного типу, літ. "A-1"` | Known from drawing title | `Materials/Plans/house-floor-plan_M100_IMG_1737.jpg` | High | One-story house. |
| Floor count | 1 floor | Known from drawing | `Materials/Plans/house-floor-plan_M100_IMG_1737.jpg` | High | Matches photos. |
| Floor plan scale | M 1:100 | Known from drawing | `Materials/Plans/house-floor-plan_M100_IMG_1737.jpg` | High | Photo of plan, not CAD. |
| Site plan scale | M 1:500 | Known from drawing | `Materials/Plans/site-plan-house-position_M500_IMG_1736.jpg` | High | Photo of plan, not CAD. |
| House main footprint | 12.72 x 11.85 m | Known from drawings/Figma | `site-plan-house-position_M500_IMG_1736.jpg`, `house-floor-plan_M100_IMG_1737.jpg`, Figma | High | Coordination value: 12.72 m. 12.74 m red markup is a field-check note only. |
| Terrace on plan | 6.30 x 3.05 m, area label 6.6 for adjacent room/zone visible | Known from drawing | `house-floor-plan_M100_IMG_1737.jpg` | Medium | Coordination envelope: 6.30 x 3.05 m. Figma 3.04 m is close enough for planning, but not for purchase cuts. |
| Canopy on plan | 3.54 m width, long side approx. 10.93 / 8.81 labels visible | Known from drawing | `site-plan-house-position_M500_IMG_1736.jpg` | Medium | Figma uses 3.54 x 11.85 m as canopy object. |
| Building height label | `H=3.87` on site/house diagram | Known from drawing | `site-plan-house-position_M500_IMG_1736.jpg` | Medium | Needs meaning confirmation before using for elevations. |
| Interior room areas | Room labels include 6.2, 9.1, 13.6, 18.0, 12.7, 6.6, 13.9, 8.1, 15.8, 7.8 m2 | Known from drawing image | `house-floor-plan_M100_IMG_1737.jpg` | Medium | Useful for house record only; not needed for exterior lighting unless routing indoors. |
| Interior heights | Several rooms show h=2.95, h=2.38, h=2.35 | Known from drawing image | `house-floor-plan_M100_IMG_1737.jpg` | Medium | Do not infer exterior soffit heights from this. |
| Well | `скважина` / well marked near upper site/behind house | Known from plan/Figma | `marked-measured-site-plan.jpg`, Figma | Medium | Exact field position and service clearance need confirmation. |
| Septic pits | `стічні ями` marked near lower/right site | Known from plan | `marked-measured-site-plan.jpg` | Medium | Must not block access with planting/lighting/hardscape. |
| Gate / wicket | Gate and wicket marked on plan/Figma | Known from plan/Figma/photos | `marked-measured-site-plan.jpg`, Figma, `front-yard-gate-and-entry_IMG_1842.jpg` | Medium | Cable routes and gate lighting still missing. |
| North orientation | Not found | Missing | No reliable north arrow found | Low | Required for final sun/shade, plant selection, privacy, overheating, daylight visuals. |

## Raw Photo Intake

| Zone | Primary raw files | Observed existing conditions | Protected / risk notes |
| --- | --- | --- | --- |
| Front entry facade | `Materials/main-entry-front-facade_IMG_1841.jpg`, `Materials/main-entry-facade-with-carport_IMG_1918.jpg`, `Materials/front-yard-gate-and-entry_IMG_1842.jpg` | One-story house, dark low-slope roof, light unfinished/plastered facade, dark front door, front steps, white/light window frames, gutter/downspouts, raw grass/sandy yard, overhead utility pole/lines near front yard | Preserve roof, front door/opening, windows, wall positions. Step redesign needs field levels and drainage check. |
| Canopy / carport | `Materials/carport-front-and-entry-edge_IMG_1843.jpg`, `Materials/carport-side-with-ac_IMG_1844.jpg`, `Materials/carport-rear-corner_IMG_1912.jpg`, `Materials/carport-rear-edge_IMG_1913.jpg` | Long covered side canopy, dark columns/beams, exposed wood structure, car parking, dirt/sandy ground, clutter, gutters/downspouts, AC unit visible near canopy side | Preserve column rhythm and AC. Lighting/hardscape must allow AC service and downspout management. Do not cut beams for downlights. |
| Terrace | `Materials/terrace-rear-wide-view_IMG_1837.jpg`, `Materials/terrace-rear-angle-from-yard_IMG_1838.jpg`, `Materials/terrace-left-wide-side-view_IMG_1839.jpg`, `Materials/terrace-front-close-view_IMG_1845.jpg`, `Materials/terrace-green-wall-and-column_IMG_1846.jpg`, `Materials/terrace-side-from-carport_IMG_1914.jpg` | Raised terrace slab, two existing door blocks to terrace, green wall, exposed/unfinished soffit, dark columns/beams, temporary garland/wires, clutter, raw plinth/base, existing small steps | Preserve doors/windows/roof/columns. Wood cladding and soffit must include cable access, ventilation, water detailing, and step level check. |
| Back yard / garden | `Materials/back-yard-wide-garden-view_IMG_1915.jpg`, `Materials/back-yard-open-lawn-and-fence_IMG_1916.jpg` | Large grassy/sandy yard, fence, neighboring buildings/trees, sandbox/play area, gravel pile, open planting potential | Planting and lighting are not final without sun orientation, soil, irrigation, drainage, and mature-size checks. |
| Service side / utility | `Materials/service-passage-side-wall_IMG_1840.jpg`, `Materials/service-building-and-side-yard_IMG_1920.jpg`, `Materials/service-side-house-wall_IMG_1921.jpg`, `Materials/service-yard-open-passage_IMG_1919.jpg` | Narrow service passage, downspouts, firewood/storage structure, grass/sandy soil, house wall/window, fence/gate context | Maintain access to downspouts, utilities, well/septic covers, service routes. Avoid blocking with shrubs/lights. |

## Protected Geometry Register

| Element | Status | Evidence | Confidence | Rule |
| --- | --- | --- | --- | --- |
| Roof shape and slope | Observed / Known in plan | Raw photos, `site-plan-house-position_M500_IMG_1736.jpg`, Figma | High | Do not change. |
| Roof overhangs / gutters / downspouts | Observed | Raw photos | High | Keep function; verify drainage before planting/hardscape. |
| Existing windows | Observed / Known in plan | Raw photos, Figma window nodes, floor plan | High for location/count, medium for exact size | Do not move, recolor, resize, or reshape unless explicitly approved. |
| Existing doors | Observed / Known in plan | Raw photos, Figma door nodes, floor plan | High | Do not change without approval. Terrace has two existing door blocks. |
| Column rhythm | Observed / Known in Figma | Canopy/terrace photos, 6 Figma column nodes | High | Do not move/reshape visually or physically without review. |
| Wall positions / massing | Observed / Known in plan | Photos, Figma, drawings | High | Preserve. |
| AC unit | Observed | `Materials/carport-side-with-ac_IMG_1844.jpg` and canopy-side photos | High for presence, medium for exact service envelope | Keep, maintain airflow/service, do not hide behind planting or sealed screen. |
| Plinth/base | Observed | Photos | Medium | Finish proposals must handle splashback, freeze-thaw, and drainage. |
| Grade/drainage relationship | Partly observed | Photos show soil/grass close to base and downspouts | Low/medium | Missing final slopes and discharge paths. |

## Style Reference Intake

User stated the house style and lighting in `Materials/References` are strongly liked.

| Reference files | Use as | Good to keep | Do not copy literally |
| --- | --- | --- | --- |
| `mood-board-materials-lighting-and-planting.jpg`, `carport-lighting-concept-front.jpg`, `carport-lighting-concept-under-canopy.jpg`, `carport-lighting-concept-side-path.jpg`, `evening-house-lighting-wide-view.jpg`, `evening-terrace-and-carport-reference.jpg`, `evening-garden-path-and-facade-reference.jpg`, `mood-board-warm-modern-exterior-views.jpg` | Mood/style references only | Warm greige facade mood, dark graphite-brown roof/metal, natural wood portals/soffits, low-glare layered lighting, soft blue-hour ambience, gravel/ornamental grasses, restrained organic modern feel | Changed windows/doors, changed roof geometry, continuous roof-outline LED, LED on every beam, 3000K equipment/specs, overlit hotel facade, excessive bollards/uplights, stone/wood massing that changes house proportions |

Reference filter:

- Accept: warmth, material mood, gentle layered light, low glare, wood + greige + dark metal + grasses.
- Reject or rewrite: `2700-3000K` labels become 2700K max; repeated 3000K fixture cards become 2700K; continuous perimeter roofline becomes separated facade/canopy/terrace zones; any altered windows/doors/roof/columns are ignored.

## Owner Clarification Intake: 2026-07-01 House-Only Architecture

| Item | Value | Status | Source | Confidence | Notes / Check |
| --- | --- | --- | --- | --- | --- |
| Current scope | Describe the house appearance only, without lighting | User-provided | Owner message 2026-07-01 | High | Lighting/electrical docs remain separate and should not drive this brief. |
| House visual direction | Describe according to references if not already documented | User-provided | Owner message 2026-07-01 + `Materials/References` | High | Use references for mood/materials only, not geometry changes. |
| Stairs / podiums | Stairs from both sides must be on the Figma plan | User-provided | Owner message 2026-07-01 | Medium/high | Working interpretation: main entry side + terrace side. If owner meant extra side stairs, request marked-up location. |
| Terrace wall by two doors | Terrace side where two doors are located should be clad with wood | User-provided | Owner message 2026-07-01 | High | Preserve door/window geometry and color. |
| Short terrace wall | Shorter / return wall should be in the facade color | User-provided | Owner message 2026-07-01 | Medium/high | Need exact wall plane confirmed on photo/plan before contractor execution. |
| House-only output file | `Exterior_Lighting_Project/01_Architectural_Zones/00_House_Exterior_Brief.md` | Known | Created 2026-07-01 | High | Source-backed owner/design brief, not construction drawing. |

## Existing Documentation Summary

| Existing file / folder | What is already documented | Current source-register note |
| --- | --- | --- |
| `Exterior_Lighting_Project/00_README.md` | Overall lighting/material concept and Figma dimensions | Strong base. Needs cross-reference to this source register before final construction use. |
| `Exterior_Lighting_Project/01_Architectural_Zones/00_House_Exterior_Brief.md` | House-only exterior architecture brief without lighting | Current owner clarification package for facade, terrace wood, shorter wall, and stairs on Figma. |
| `Exterior_Lighting_Project/01_Design_Concept.md` | Organic modern direction, materials, zones, key avoid list | Aligned with references and project rule. |
| `Exterior_Lighting_Project/02_Electrical_and_Home_Assistant.md` | HA dimming logic, 24V/PWM/DALI alternatives, scenes, safety basics | Good planning guidance. Electrical capacity and routing still missing. |
| `Exterior_Lighting_Project/03_Power_Line_Schedule.md` | Neon/downlight lines, estimated powers, PSU sizing | Useful draft. Needs segment length conflict resolved before purchase. |
| `01_Architectural_Zones/*/00_Brief.md` | Detailed main entry, canopy, terrace briefs and prompts | Good; visualization prompts still need preservation constraints and conflict filtering when reused. |
| `02_Landscape/00_README.md` | Draft landscape lighting zones | Placeholder only. Needs sun/soil/drainage/irrigation before plant/fixture plan. |
| `04_Equipment_Selection` | Candidate equipment comparisons | Very early. No final owner selection. |
| `05_Purchase_Bill_of_Materials` | Draft BOM quantities | Planning quantities only, not purchase-ready. |
| `03_Estimate` | Budget placeholders | Not a current estimate. No prices verified. |

## Resolved Dimension Coordination Rules

| Item | Coordination value | Resolution | Still required |
| --- | ---: | --- | --- |
| Main house long facade | 12.720 m | Resolved for coordination. 12.72 m appears in Figma and official-looking plan/drawing sources; 12.74 m is treated as a +20 mm field-check variance, not a separate design dimension. | Field measure before ordering exact-length LED, cladding, flashing, stone, or profiles. |
| Terrace slab envelope | 6.30 x 3.05 m | Resolved for coordination. Use the plan value 3.05 m as the nominal envelope; Figma 3.040 m is a 10 mm model variance; 3.0 m markup is treated as rounded shorthand. | Field measure finished/structural slab before tile, wood, step, profile, or lighting purchases. |
| Canopy neon N2 / L2 | 12.645 m total; 3 x ~4.215 m planning segments | Resolved for coordination. The old `3 x ~3.95 m` note was incorrect for the 12.645 m line; use `3 x ~4.215 m` or rounded `3 x ~4.22 m` in planning docs. | Electrician/installer must confirm field length, product cut interval, voltage drop, feed points, junction access, and whether 2-end feed or middle feed is better. |

## Conflict And Resolution Register

| Issue | Sources | Recommendation | What to check before implementation |
| --- | --- | --- | --- |
| Site size is not consistently represented as a simple rectangle: old README says approx. 25.25 x 44.45 m; Figma frame is 25.25 x 44.09 m; boundary vector is approx. 25.25 x 44.446 m; plan shows a polygon with 33.67 / 44.09 / 25.25 and a broken roadside edge. | `Exterior_Lighting_Project/00_README.md`, Figma node `8:154`, `Materials/Plans/*.jpg` | Treat site as survey polygon, not a rectangle. Use the survey/plan photo or CAD if available for boundaries. | Obtain original survey/CAD or confirm boundary dimensions on site before site plan, irrigation, planting counts, or fence/lighting layout. |
| House facade length variance: 12.72 m in Figma/drawings, 12.74 m in one red markup. | Figma, `site-plan-house-position_M500_IMG_1736.jpg`, `house-floor-plan_M100_IMG_1737.jpg`, `marked-measured-site-plan.jpg` | Resolved for coordination: use 12.720 m. Treat 12.74 m as a +20 mm field-check variance, not a blocking conflict. | Field measure the relevant facade line with laser/roulette before exact material cuts. |
| Terrace depth variance: 3.04 m in Figma, 3.05 m on plan, 3.0 m in one red markup. | Figma, `house-floor-plan_M100_IMG_1737.jpg`, `marked-measured-site-plan.jpg` | Resolved for coordination: use 6.30 x 3.05 m as the nominal planning envelope. Treat 3.04 m as model variance and 3.0 m as rounded shorthand. | Measure finished/structural terrace slab before tile, wood, steps, and lighting profiles. |
| Canopy neon segmentation variance: old carport brief said 3 segments of ~3.95 m, while 12.645 m divided by 3 is ~4.215 m and the power schedule used ~4.22 m. | `01_Architectural_Zones/02_Carport/00_Brief.md`, `03_Power_Line_Schedule.md`, Figma `Гнучкий неон Навіс 2 24В` 12.645 m | Resolved for coordination: use 12.645 m total, planning segmentation 3 x ~4.215 m, rounded to 3 x ~4.22 m. | Check actual product cut length, voltage drop, feed points, and accessible junction boxes before purchase/cut. |
| References often show 2700-3000K and equipment cards marked 3000K, but project rule is warm white 2700K with 3000K maximum only as upper bound. | `Materials/References/*.jpg`, `AGENTS.md`, existing lighting docs | Use references for mood, not temperature specs. Specify 2700K for all exterior lighting unless a rare exception is explicitly approved. | Verify fixture CCT at low dimming levels and reject yellow neon/RGB/cold white. |
| References and some prompt language show long continuous roof/terrace lines, but project rules reject a full roof outline and LED skeleton. | References, `04_Visualization_Prompts.md`, terrace/canopy briefs | Keep separate light scenes: front facade line, canopy outer-beam line, terrace step/soft soffit line only if restrained. No full perimeter outline. | Architecture + lighting review before final prompts and before installing profiles. |
| Figma contains many lighting objects: 12 ground lights, 28 plant uplights, 20 220V poles. Existing design direction says restrained, low-glare, no runway path. | Figma count summary, `02_Landscape/00_README.md`, references | Treat Figma lighting objects as candidate/brainstorm inventory, not final fixture schedule. | Run landscape + lighting coordination after plant masses, paths, drainage, and cable routes are known. |
| AC unit could conflict with future slatted screens, planting, technical cabinet, or canopy lights. | Raw canopy photos, protected house rule | Preserve AC access and airflow. Any screen must be ventilated, removable/accessible, and not trap heat. | Confirm required clearances, condensate path, service side, and whether owner wants visual softening. |
| Landscape/plant references assume planting types but sun, soil, irrigation, and drainage are missing. | References, photos, missing orientation/soil data | Do not finalize plant palette. Use references for mood only. | Confirm north/facade orientation, sun exposure, soil/drainage, water source, irrigation plan, maintenance tolerance. |

## Missing Fact Register

| Topic | Status | Needed for | How to verify |
| --- | --- | --- | --- |
| North orientation / facade orientation | Missing | Sun analysis, plants, terrace comfort, daylight visualizations | Compass/map screenshot, survey plan with north arrow, or geolocated plan |
| Official CAD/survey source | Missing | Accurate site plan, boundaries, quantities | Ask owner / export from surveyor |
| Field dimensions for facade, canopy, terrace, steps | Missing | LED lengths, cladding, hardscape, cost | Laser/roulette measurement before purchase |
| Soil type / compaction / drainage behavior | Missing | Planting, irrigation, hardscape base, drainage | Soil test or site observation after rain |
| Downspout discharge and slope | Missing | Drainage, gravel strips, paths, foundations | Site walk, rain observation, contractor check |
| Electrical capacity, circuits, RCD/diff protection, exterior outlets | Missing | Lighting install, HA, transformers/drivers | Qualified electrician verification |
| Cable/conduit routes and sleeve locations | Missing | Avoid rework before paths/planting | Electrical + landscape route plan |
| Irrigation source/pressure and watering zones | Missing | Plant selection and survival | Water source test / irrigation plan |
| Budget ceiling and phasing preference | Missing | Must-have/should-have/later prioritization | Owner decision |
| Maintenance tolerance | Missing | Plant palette, gravel/grass balance, fixture access | Owner decision |

## Current Measurement Package

| Package | Status | Use |
| --- | --- | --- |
| `planning/orientation-survey-intake.md` | Created 2026-07-01; awaiting owner/survey/map/compass input | Confirm north orientation and source hierarchy before sun/shade, plant exposure, daylight prompts, or privacy decisions. |
| `planning/field-measurement-checklist.md` | Created 2026-07-01; awaiting field values | Confirm facade/canopy/terrace/step dimensions, AC clearance, downspouts, and electrical route constraints before lighting-doc edits, purchase quantities, or cost estimates. |
