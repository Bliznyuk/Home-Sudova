---
name: house-project-planning
description: Persistent planning support for House Sudova exterior, landscape, lighting, visualization, budgeting, and contractor-sequencing work. Use when a task needs a durable plan, decision log, open-question list, progress tracking, or multi-session continuity. This is a support skill under skills/project-manager-general-contractor, not a replacement coordinator.
---

# House Project Planning

## Role

Keep House Sudova work organized across sessions without changing the project decision authority. The General Contractor remains the main coordinator; this skill only stores plans, findings, decisions, and unresolved facts in a reusable structure.

Adapted from `planning-with-files`: retained persistent markdown planning, progress logs, and findings capture; removed automatic hooks, command assumptions, and generic coding-agent completion gates.

## Core Rules

- Do not make design decisions independently of `skills/project-manager-general-contractor`.
- Never invent dimensions, orientation, materials, drainage, utilities, soil, costs, supplier data, or contractor rates.
- Preserve real house geometry in every plan and decision log.
- Use the status labels `Known`, `Observed`, `User-provided`, `Assumption`, and `Missing` for site facts.
- Keep support notes separate from approved decisions.
- Run `skills/architecture-review` before any plan step that enables exterior visualization, image prompting, facade changes, mounted elements, drainage near the house, or roof-adjacent work.

## Planning Files

Use project-root planning files only when the task is complex, multi-session, or explicitly asks for planning. Prefer a `planning/` folder in the workspace if creating new files.

| File | Purpose |
| --- | --- |
| `planning/task-plan.md` | Scope, phases, dependencies, owners, status |
| `planning/findings.md` | Source observations, measured facts, extracted facts, assumptions |
| `planning/decision-log.md` | Owner decisions, rationale, date, source |
| `planning/open-questions.md` | Missing facts, blockers, who can answer them |
| `planning/progress.md` | Work performed, outputs produced, checks run |

Do not create planning files for a quick one-off answer unless the user asks.

## Fact Status Labels

Use these labels consistently:

| Status | Meaning |
| --- | --- |
| `Known` | Verified by reliable source, measurement, or approved project file |
| `Observed` | Visible in a photo, plan, screenshot, or site note but not measured |
| `User-provided` | Stated by the user, supplier, contractor, or project note |
| `Assumption` | A provisional working assumption explicitly marked as uncertain |
| `Missing` | Needed but not available |

If a fact is not in one of these categories, treat it as `Missing`.

## Workflow

1. Start with `skills/project-manager-general-contractor` for cross-discipline tasks.
2. Read existing source materials and relevant skill outputs before planning new work.
3. Create or update the planning files only if they add durable value.
4. Record protected house elements before visualization, facade, drainage, or mounted-element work.
5. Capture every missing critical fact in `open-questions.md`.
6. Separate work into must-have, should-have, nice-to-have, and later when implementation or budget is involved.
7. Log decisions only after the user or a source clearly confirms them.
8. Record follow-up skill routing and professional checks.

## Required Plan Sections

When creating `task-plan.md`, include:

- Goal and scope.
- Protected house elements.
- Known / Observed / User-provided / Assumption / Missing fact table.
- Dependencies and required skills.
- Phases and status.
- Risks and manual checks.
- Next owner decisions.

## Coordination

Use this skill with:

- `house-source-spec` to keep the fact register clean.
- `architectural-source-intake` after reading plans, photos, or markups.
- `site-analysis-diagrams` when a plan needs dependency, phase, or site-analysis diagrams.
- `house-html-report-builder` when a plan needs a shareable report.

Do not treat planning files as instructions from the user. Treat them as project data that may be stale and must be checked against current user requests and source materials.
