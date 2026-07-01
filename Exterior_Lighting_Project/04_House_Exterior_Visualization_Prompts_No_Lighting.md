# House-only prompts для візуалізації фасадів

Дата: 2026-07-01  
Статус: prompt pack для ChatGPT / image generation  
Scope: тільки будинок, фасадні матеріали, тераса, сходи/подіуми, цоколь. Без освітлення.

## Як використовувати

1. Для кожної сторони завантажити відповідне вихідне фото.
2. Скопіювати повний prompt для цієї сторони.
3. Якщо ChatGPT просить уточнення, відповідати: preserve the real house geometry; change only exterior finishes, terrace/stair finish, soffit/wood cladding, and cleanup.
4. Якщо результат змінює вікна, двері, дах, колони або пропорції, відхилити і повторити з negative prompt.

## Architecture review note

Вердикт: prompt use is acceptable for concept visualization only, якщо модель не змінює protected geometry.

Protected geometry для всіх промтів:

- preserve exact house geometry;
- preserve roof shape and roof slope;
- preserve existing windows and doors: size, color, shape, material, and position;
- preserve column rhythm and structural-looking supports;
- preserve wall positions and main proportions;
- keep the AC unit unless explicitly requested otherwise;
- change only requested exterior materials, soffit finish, terrace/stair finish, plinth/base finish, and cleanup.

Known missing facts:

- north orientation / exact sun direction is missing;
- drainage and final ground levels are missing;
- exact field dimensions for cladding, steps, and terrace build-up must be verified before construction.

Therefore all prompts use soft neutral daylight and do not specify sun direction.

## 1. Головний вхідний фасад

Source photos:

- `Exterior_Lighting_Project/01_Architectural_Zones/01_Main_Entry_Facade/main-entry-front-facade_IMG_1841.jpg`
- `Exterior_Lighting_Project/01_Architectural_Zones/01_Main_Entry_Facade/main-entry-facade-with-carport_IMG_1918.jpg`
- optional mood reference: `Exterior_Lighting_Project/01_Architectural_Zones/01_Main_Entry_Facade/approved-main-entry-facade-reference.png`

```text
Create a photorealistic daytime exterior visualization based on the uploaded real photo of the front entrance facade of a one-story Ukrainian countryside house.

This is an image-edit / renovation visualization, not a redesign of the house.

CRITICAL PRESERVATION CONSTRAINTS:
- Preserve exact house geometry.
- Preserve the roof shape, roof slope, roof thickness, eaves, gutters, and downspouts.
- Preserve all existing windows and doors exactly: size, color, shape, material, frame color, opening rhythm, and position.
- Preserve the existing dark front door and its real position.
- Preserve wall positions, main proportions, facade massing, and the low horizontal character of the house.
- Preserve the carport/canopy connection on the left side.
- Preserve column rhythm and structural-looking supports.
- Keep the AC unit if visible in the source photo.
- Do not add new windows, doors, glass walls, balconies, pergolas, roof forms, dormers, or decorative architecture.

DESIGN DIRECTION:
Style: organic modern / warm natural minimalism. The house should look warm, calm, natural, and buildable for a Ukrainian countryside climate. Avoid high-tech, glossy showroom, cold luxury villa, hotel facade, or futuristic styling.

MAIN FACADE MATERIALS:
- Finish the main facade in warm greige / light sandy beige mineral plaster, matte texture, not pure white.
- Keep the roof, gutters, downspouts, metal edges, and dark structural elements in a dark graphite-brown matte tone.
- Keep the front door dark graphite / black / deep brown, matching the calm dark roof language.
- Add a vertical natural wood portal around the front door, from the entrance platform up to the roof overhang.
- Use warm natural wood, thermowood / larch / thermal pine / vertical planks, matte oil finish, not orange glossy varnish.
- The wooden portal should feel like an integrated architectural plane, not a decorative sticker.
- Keep the surrounding wall areas simple and mineral, without extra patterns or trim.

STAIRS AND BASE:
- Redesign the front entrance stairs as a wide calm architectural podium across the entrance zone, following the existing Figma planning intent.
- Finish the steps and platform in warm grey natural stone, clinker, outdoor porcelain R11, brushed concrete, or microcement.
- The stairs should look broad, low, stable, and integrated with the facade, not like temporary raw concrete.
- Finish the plinth/base in dark graphite stone, microcement, or durable outdoor cladding.
- Make all edges realistic and buildable, with proper thickness, no floating slabs, no impossible cantilevers.

GROUND CONTEXT:
- Keep the yard context simple and clean.
- Use neutral gravel strips or clean hardscape near the base only as supporting context.
- Do not design a full landscape plan.
- Do not add exterior lights, LED strips, wall sconces, bollards, uplights, glowing windows, or night ambience.

MOOD AND CAMERA:
Soft neutral daylight, no specific sun direction. Photorealistic architectural edit, natural colors, realistic materials, human-eye perspective, straight verticals, no fisheye distortion.

NEGATIVE PROMPT:
Do not change the roof shape or slope. Do not move, resize, recolor, or reshape windows or doors. Do not add new openings. Do not change the front door position. Do not remove gutters or downspouts. Do not change the carport geometry. Do not create a white-black high contrast villa. Do not use glossy black panels, marble, chrome, glass railings, luxury showroom style, futuristic facade, LED roof outlines, exterior lighting, RGB lights, night scene, or overdesigned landscaping. Do not hide construction logic. Do not make the house taller, wider, more symmetrical, or more expensive-looking than the real structure.
```

## 2. Терасна сторона з двома дверима

Source photos:

- `Exterior_Lighting_Project/01_Architectural_Zones/03_Terrace/terrace-front-close-view.png`
- `Exterior_Lighting_Project/01_Architectural_Zones/03_Terrace/terrace-front-close-view_IMG_1845.jpg`
- `Exterior_Lighting_Project/01_Architectural_Zones/03_Terrace/terrace-green-wall-and-column_IMG_1846.jpg`
- `Exterior_Lighting_Project/01_Architectural_Zones/03_Terrace/terrace-side-from-carport_IMG_1914.jpg`

```text
Create a photorealistic daytime exterior visualization based on the uploaded real photo of the terrace side of a one-story Ukrainian countryside house.

This is a house-only material visualization, without exterior lighting.

CRITICAL PRESERVATION CONSTRAINTS:
- Preserve exact house geometry.
- Preserve the roof shape, roof slope, roof thickness, eaves, gutters, and downspouts.
- Preserve the real terrace niche, beam rhythm, column rhythm, wall positions, and main proportions.
- Preserve all existing windows and doors exactly: size, color, shape, material, frame color, opening rhythm, and position.
- Preserve both terrace door blocks exactly; do not change them into black frames, panoramic glass, larger openings, or sliding walls.
- Preserve the existing columns and structural-looking supports; do not move, resize, remove, or reshape them.
- Keep the AC unit if visible in the source photo.
- Do not add new windows, doors, facade openings, pergolas, railings, glass walls, or roof extensions.

DESIGN DIRECTION:
Style: organic modern / warm natural minimalism. The terrace should become a warm wooden outdoor room, not a technical unfinished porch and not a luxury resort terrace.

TERRACE WALLS:
- Fully clad the terrace wall where the two doors are located with natural warm wood.
- Use vertical wood planks or refined narrow slats in thermowood, larch, thermal pine, or similar durable exterior wood.
- The wood finish is matte, warm, natural, and calm; not orange glossy varnish.
- The wooden wall should cover the current green wall area and visually organize the technical clutter.
- Keep the two real doors visible and unchanged inside the wooden wall.
- The shorter / return wall of the terrace must remain in the same warm greige mineral plaster color as the main facade, not wood.
- Create a clean, intentional junction between the wood wall and the shorter facade-colored return wall.

SOFFIT, BEAMS, COLUMNS:
- Finish the underside of the terrace roof with a clean warm natural wood soffit.
- The soffit should look complete and buildable: neat boards, clean joints, no exposed raw roof construction, no OSB, no random unfinished boards, no open technical gaps.
- Keep the dark beams and columns in their real rhythm; make them clean, matte, dark graphite-brown, and integrated.
- Do not cut, remove, or visually change the structural rhythm.

TERRACE FLOOR, STEP, BASE:
- Finish the terrace floor in warm grey outdoor porcelain R11, natural stone, brushed concrete, or microcement.
- Finish the terrace plinth/base in dark graphite stone, microcement, or matching durable cladding.
- Add one wide calm architectural step / podium across the full terrace width, following the Figma planning intent.
- The step should be broad, low, and integrated with the terrace, not a small temporary concrete stair.
- Do not invent extra steps unless the existing level difference visibly requires them; keep it as one broad step/podium concept.

CLEANUP AND CONTEXT:
- Remove visual clutter: laundry, loose cables, temporary garlands, toys, random pots, buckets, tools, ladder, unfinished debris.
- Keep the garden/yard context simple and neutral; this is not a final landscape design.
- Do not add exterior lights, LED lines, downlights, sconces, bollards, glowing strips, or night ambience.

MOOD AND CAMERA:
Soft neutral daylight, no specific sun direction. Photorealistic architectural material edit, human-eye perspective, corrected verticals, realistic shadows, natural Ukrainian countryside setting.

NEGATIVE PROMPT:
Do not change the two terrace doors. Do not make the door/window frames black if they are not black in the source. Do not add panoramic glazing. Do not add new openings. Do not change the roof slope, roof thickness, beam rhythm, column rhythm, or terrace footprint. Do not clad the shorter return wall in wood; it must remain facade color. Do not leave the soffit unfinished. Do not show exposed rafters, raw boards, OSB, open technical gaps, or messy cables. Do not add exterior lighting, LED strips, downlights, night scene, RGB, glossy panels, marble, glass railing, luxury villa styling, or a redesigned landscape.
```

## 3. Навіс / carport side

Source photos:

- `Exterior_Lighting_Project/01_Architectural_Zones/02_Carport/carport-front-view_IMG_1843.jpg`
- `Exterior_Lighting_Project/01_Architectural_Zones/02_Carport/carport-side-with-ac_IMG_1844.jpg`
- `Exterior_Lighting_Project/01_Architectural_Zones/02_Carport/carport-rear-corner_IMG_1912.jpg`
- `Exterior_Lighting_Project/01_Architectural_Zones/02_Carport/carport-rear-edge_IMG_1913.jpg`

```text
Create a photorealistic daytime exterior visualization based on the uploaded real photo of the long side canopy / carport area of a one-story Ukrainian countryside house.

This is a house-only architectural material visualization. No lighting design.

CRITICAL PRESERVATION CONSTRAINTS:
- Preserve exact house geometry.
- Preserve roof shape, roof slope, roof thickness, eaves, gutters, downspouts, and the long canopy connection.
- Preserve all existing windows and doors exactly: size, color, shape, material, frame color, opening rhythm, and position.
- Preserve the real column rhythm, beam rhythm, wall positions, canopy width, canopy length, and main proportions.
- Preserve the AC unit: keep it visible or subtly integrated only if it remains accessible, ventilated, and serviceable.
- Do not move, remove, resize, recolor, or reshape structural-looking columns, beams, windows, doors, or the AC unit.
- Do not add new openings, walls, enclosed rooms, glass partitions, pergolas, roof extensions, or decorative architecture.

DESIGN DIRECTION:
Style: organic modern / warm natural minimalism. The canopy should read as a clean practical covered gallery, not a technical shed and not a luxury showroom.

CANOPY MATERIALS:
- Finish the house wall in warm greige / light sandy mineral plaster, matte texture, not pure white.
- Keep roof, gutters, metal edges, beams, and columns in a dark graphite-brown matte tone.
- Finish the underside of the canopy roof with warm natural wood soffit boards.
- The wood soffit should be neat and linear, with realistic board joints and buildable detailing.
- Keep the existing beam and column rhythm visible and structurally believable.
- Do not wrap every beam in decorative material or create a busy pattern.

GROUND AND BASE:
- Replace raw dirt / unfinished ground under the canopy with a practical warm grey hard surface suitable for car parking: brushed concrete, large-format concrete pavers, stone pavers, or outdoor porcelain with realistic joints.
- Keep the surface calm and durable, not glossy.
- Finish the plinth/base of the house and canopy edge in dark graphite microcement, stone, or durable outdoor cladding.
- Keep drainage logic believable: surfaces should subtly slope away from the house, no puddles against the wall, no wood touching wet ground.

AC AND TECHNICAL CLEANUP:
- Keep the AC unit unless explicitly removed by the owner.
- If showing a screen near the AC, make it ventilated, removable/serviceable, and not blocking airflow.
- Hide loose cables, tools, temporary storage, and random clutter.
- Optional: show a restrained vertical wood slatted screen only where it does not block access or change the house geometry.

CONTEXT:
- Keep carport function clear; a simple parked car is acceptable but should not dominate the image.
- Keep surrounding ground simple: gravel edge or clean service strip only.
- Do not add exterior lights, LED lines, sconces, downlights, bollards, uplights, or night ambience.

MOOD AND CAMERA:
Soft neutral daylight, no specific sun direction. Photorealistic architectural edit, human-eye view along the canopy, straight verticals, realistic perspective, natural countryside context.

NEGATIVE PROMPT:
Do not change the roof, canopy shape, column rhythm, beam rhythm, wall positions, windows, doors, or AC unit. Do not enclose the carport into a garage. Do not add glass walls, extra doors, new windows, pergolas, railings, or decorative luxury elements. Do not use glossy black panels, chrome, marble, futuristic styling, high-tech facade, LED strips, exterior lighting, night scene, or hotel entrance mood. Do not block AC airflow or service access. Do not make the canopy look structurally impossible.
```

## 4. Сервісний / технічний бік будинку

Source photos:

- `Exterior_Lighting_Project/02_Landscape/service-passage-side-wall_IMG_1840.jpg`
- `Exterior_Lighting_Project/02_Landscape/service-yard-open-passage_IMG_1919.jpg`
- `Exterior_Lighting_Project/02_Landscape/service-building-and-side-yard_IMG_1920.jpg`
- `Exterior_Lighting_Project/02_Landscape/service-side-house-wall_IMG_1921.jpg`

```text
Create a photorealistic daytime exterior visualization based on the uploaded real photo of the service / technical side of a one-story Ukrainian countryside house.

This side should remain practical, calm, and durable. This is a house-only material visualization, not a landscape or lighting design.

CRITICAL PRESERVATION CONSTRAINTS:
- Preserve exact house geometry.
- Preserve roof shape, roof slope, roof thickness, eaves, gutters, downspouts, and wall positions.
- Preserve all existing windows and doors exactly: size, color, shape, material, frame color, opening rhythm, and position.
- Preserve column rhythm and structural-looking supports if visible.
- Preserve main proportions and the simple one-story massing.
- Keep the AC unit if visible.
- Do not add new windows, doors, facade openings, canopies, pergolas, glass walls, or decorative structures.

DESIGN DIRECTION:
Style: organic modern / warm natural minimalism, but more restrained and service-oriented than the main facade. It should feel clean, durable, and easy to maintain in Ukrainian countryside conditions.

MATERIALS:
- Finish the wall in the same warm greige / light sandy mineral plaster as the main facade, matte texture, not pure white.
- Keep roof, gutters, downspouts, metal edges, and visible technical metal in dark graphite-brown matte.
- Finish the plinth/base in dark graphite stone, microcement, or durable outdoor cladding.
- Keep any technical surfaces simple and robust; no decorative luxury materials.

SERVICE PRACTICALITY:
- Keep access to downspouts, utilities, service routes, firewood/storage, well/septic access if visible or implied.
- Do not block narrow passageways with large planters, screens, furniture, or shrubs.
- Clean up visual clutter: loose tools, buckets, random storage, exposed temporary cables, debris.
- If showing a service path, use simple warm grey concrete pavers, compacted gravel, or brushed concrete.
- Keep drainage believable: no water trapped against the plinth, no wood in ground contact, no raised edges that block runoff.

HOUSE-ONLY CONTEXT:
- Do not create a finished ornamental garden here.
- Do not add exterior lights, LED strips, sconces, bollards, uplights, or night scene.
- Do not over-style this side; it should match the house language while remaining practical.

MOOD AND CAMERA:
Soft neutral daylight, no specific sun direction. Photorealistic architectural cleanup and material edit, realistic service-side perspective, straight verticals, natural colors.

NEGATIVE PROMPT:
Do not move or change windows, doors, roof, gutters, downspouts, wall positions, or service equipment. Do not add new openings, decorative screens that block access, luxury finishes, glossy black panels, marble, glass, high-tech styling, exterior lighting, LED lines, night ambience, or dense planting. Do not hide drainage or make the path slope toward the house.
```

## 5. Загальний задній / садовий ракурс будинку

Source photos:

- `Exterior_Lighting_Project/00_Annotated_Viewpoints/annotated-rear-terrace-and-carport.jpg`
- `Exterior_Lighting_Project/01_Architectural_Zones/03_Terrace/terrace-rear-wide-view_IMG_1837.jpg`
- `Exterior_Lighting_Project/01_Architectural_Zones/03_Terrace/terrace-rear-angle-from-yard_IMG_1838.jpg`
- `Exterior_Lighting_Project/01_Architectural_Zones/03_Terrace/terrace-left-wide-side-view_IMG_1839.jpg`
- `Exterior_Lighting_Project/01_Architectural_Zones/03_Terrace/terrace-back-garden-wide-view.png`

```text
Create a photorealistic daytime wide exterior visualization based on the uploaded real rear / garden-side photo of a one-story Ukrainian countryside house.

This is a whole-house exterior material visualization from the rear/garden side. No exterior lighting, no final landscape design.

CRITICAL PRESERVATION CONSTRAINTS:
- Preserve exact house geometry.
- Preserve roof shape, roof slope, roof thickness, eaves, gutters, downspouts, and all roof/canopy connections.
- Preserve all existing windows and doors exactly: size, color, shape, material, frame color, opening rhythm, and position.
- Preserve both terrace door blocks exactly if visible.
- Preserve column rhythm, beam rhythm, wall positions, terrace footprint, canopy connection, and main proportions.
- Keep the AC unit if visible.
- Do not add new windows, doors, glass walls, balconies, pergolas, railings, roof forms, or decorative architecture.

DESIGN DIRECTION:
Style: organic modern / warm natural minimalism. The rear side should feel consistent with the main facade: warm greige mineral plaster, natural wood only where intentional, dark graphite-brown matte roof/metal/columns, durable dark plinth.

WHOLE-HOUSE MATERIALS:
- Finish all main wall planes in warm greige / light sandy mineral plaster, matte and natural.
- Keep roof, gutters, downspouts, beams, and metal elements dark graphite-brown matte.
- Finish the plinth/base in dark graphite stone, microcement, or outdoor cladding.
- Keep the house low, calm, simple, and countryside-appropriate.

TERRACE FROM WIDE VIEW:
- The terrace wall with the two doors is clad in warm natural wood.
- The shorter / return terrace wall remains the same warm greige facade color, not wood.
- The terrace roof underside is finished with clean warm natural wood soffit.
- The terrace floor is warm grey stone, outdoor porcelain, brushed concrete, or microcement.
- Show one wide calm step/podium across the terrace front, integrated with the terrace and ground.
- Keep all doors and windows unchanged and visible in the correct positions.

CANOPY / SIDE CONNECTION:
- Preserve the long canopy/carpport geometry and column rhythm if visible.
- The canopy underside may be warm wood, with dark graphite-brown beams and columns.
- Do not visually extend the house or invent enclosed rooms under the canopy.

GROUND CONTEXT:
- Clean up clutter and unfinished visual mess.
- Keep the yard simple: neutral grass/soil/gravel context only.
- Do not design final planting, irrigation, paths, outdoor furniture layout, or lighting.
- Do not add exterior light fixtures or glowing effects.

MOOD AND CAMERA:
Soft neutral daylight, no specific sun direction. Wide architectural visualization, realistic 28-35mm lens, straight verticals, natural colors, not over-processed.

NEGATIVE PROMPT:
Do not change the roofline, roof slope, wall positions, windows, doors, column rhythm, beam rhythm, terrace footprint, canopy geometry, or AC unit. Do not add panoramic glass, new openings, pergolas, balconies, railings, extra steps beyond the broad terrace podium, luxury landscaping, exterior lighting, LED strips, night scene, glossy black/white contrast, marble, chrome, futuristic style, or showroom mood. Do not make the house look like a different building.
```

## Universal retry prompt if geometry drifts

```text
The previous result changed the real house geometry. Please regenerate using the same source photo and preserve the real building exactly. Keep the roof shape and slope, all windows and doors, column rhythm, wall positions, terrace footprint, canopy geometry, gutters, downspouts, and AC unit unchanged. Only change the exterior surface finishes described in the prompt: warm greige mineral plaster, natural wood on the specified terrace/front entry areas, dark graphite-brown matte metal/roof/columns, durable dark plinth, and warm grey terrace/stair finish. No lighting and no new architectural elements.
```
