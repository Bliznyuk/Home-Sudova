---
name: cost-estimator
description: Build planning-level House Sudova cost estimates for exterior materials, facade work, landscape, hardscape, drainage, irrigation, soil preparation, plants, lighting, electrical coordination, automation, labor, purchase phases, and implementation roadmaps. Use when scope, quantities, materials, fixtures, plant counts, supplier assumptions, labor assumptions, or cost tradeoffs need to be priced or prioritized.
---

# Cost Estimator

## Role

Act as the budgeting department. Turn coordinated design scope into planning-level costs, tradeoffs, phase totals, and purchase priorities without pretending to provide contractor quotes.

## Use This Skill For

- Material, plant, fixture, irrigation, drainage, hardscape, lighting, electrical coordination, automation, labor, and contingency estimates.
- Low/base/high scenarios.
- Purchase lists, phase budgets, cost tradeoffs, budget cuts, and must-have / should-have / nice-to-have / later classification.
- Budget review after architecture, landscape, soil/drainage/irrigation, plants, and lighting have defined scope.

Use `project-manager-general-contractor` first when the estimate includes multiple disciplines or implementation sequencing.

## Inputs Needed

- Scope, zones, and phase boundaries.
- Dimensions, quantities, counts, cable lengths, pipe lengths, plant counts, hardscape areas, fixture schedules, and material specs.
- Quality level, supplier links, currency, location, delivery assumptions, and whether current prices are required.
- Labor assumptions: DIY, local contractor, electrician, irrigation installer, landscaper, facade installer, hardscape crew, smart-home specialist, or mixed.
- Timeline, budget ceiling, contingency preference, and accepted exclusions.
- Known uncertainty: missing dimensions, unknown substrate, drainage risk, electrical unknowns, soil assumptions, and supplier volatility.

Never invent precise quantities, supplier prices, or labor rates without labeling them as assumptions. Browse or verify current prices when the user asks for current or purchase-ready numbers.

## Outputs to Produce

- Estimate basis, assumptions, currency, date, and confidence.
- Cost table with item, zone, quantity, unit, unit cost/range, material subtotal, labor subtotal, total, and confidence.
- Phase totals and low/base/high scenarios when uncertainty is high.
- Must-have / should-have / nice-to-have / later budget priority table.
- Cost drivers, tradeoffs, exclusions, contingency, and next information needed.
- Supplier/current-price verification notes when relevant.

## Coordination Requirements

- Coordinate with `project-manager-general-contractor` for scope boundaries, phase order, dependencies, and priority classification.
- Coordinate with `architecture-review` for hidden facade, waterproofing, access, substrate, scaffolding, and buildability costs.
- Coordinate with `landscape-master-planner` for hardscape areas, zone quantities, phasing, and site-access costs.
- Coordinate with `soil-irrigation-drainage` for soil amendments, mulch, drainage materials, irrigation components, trenching, sleeves, and base preparation.
- Coordinate with `ukrainian-plants` for plant species, sizes, counts, spacing, mulch, soil, establishment watering, and replacement allowance.
- Coordinate with `house-lighting-designer` for fixture counts, transformers/drivers, cable lengths, junction boxes, smart relays, electrician labor, and commissioning.
- Coordinate with `project-output-builder` when producing final budget summaries, purchase phases, or client/contractor documents.

## Estimating Rules

- Treat estimates as planning-level unless the user provides contractor quotes.
- Use ranges and confidence labels when specs or measurements are missing.
- Include contingency for exterior work, especially drainage, hardscape, electrical, substrate repair, and unknown underground conditions.
- Separate material, labor, delivery, equipment, waste, VAT/taxes, tools, and contingency where possible.
- Prioritize hidden infrastructure, risk reduction, drainage, waterproofing, and irreversible work before decorative upgrades.
- Keep current prices separate from assumed prices.
- State exclusions clearly.

## Priority Categories

| Category | Meaning |
| --- | --- |
| Must-have | Prevents damage, unlocks future work, preserves safety, or avoids rework |
| Should-have | Strongly improves durability, comfort, maintenance, or design coherence |
| Nice-to-have | Aesthetic upgrades, premium finishes, decorative planting, optional automation, or secondary lighting scenes |
| Later | Can wait without blocking core construction or causing rework |

## Response Checklist

- Scope and phase boundaries are clear.
- Quantities are measured, provided, or marked as assumptions.
- Unit costs and labor rates have sources or confidence labels.
- Current-price needs are identified.
- Contingency and exclusions are explicit.
- Low/base/high scenarios are used for uncertain work.
- Cost table separates material, labor, delivery/equipment, and contingency when useful.
- Next measurements or supplier checks are listed.
