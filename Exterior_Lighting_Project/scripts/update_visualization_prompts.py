#!/usr/bin/env python3
"""Build the visualization prompt index from each architectural zone TZ file."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]
WORKSPACE_DIR = PROJECT_DIR.parent
ZONES_DIR = PROJECT_DIR / "01_Architectural_Zones"
OUTPUT_PATH = PROJECT_DIR / "04_Visualization_Prompts.md"

PROMPT_HEADING = "## Промт для візуалізації"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def view_title(tz_text: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+?)(?::|$)", tz_text, flags=re.MULTILINE)
    if match:
        return match.group(1).strip()

    title = re.sub(r"^\d+_", "", fallback).replace("_", " ").strip()
    return title or fallback


def extract_prompt_section(tz_text: str) -> str | None:
    start = tz_text.find(PROMPT_HEADING)
    if start == -1:
        return None

    content_start = tz_text.find("\n", start)
    if content_start == -1:
        return ""

    section = tz_text[content_start + 1 :]
    next_heading = re.search(r"^##\s+", section, flags=re.MULTILINE)
    if next_heading:
        section = section[: next_heading.start()]

    section = section.strip()
    if not section or "```text" not in section:
        return None

    return section


def collect_prompts() -> tuple[list[tuple[str, Path, str]], list[Path]]:
    prompts: list[tuple[str, Path, str]] = []
    missing: list[Path] = []

    for tz_path in sorted(ZONES_DIR.glob("*/00_Brief.md")):
        tz_text = read_text(tz_path)
        prompt = extract_prompt_section(tz_text)
        if prompt is None:
            missing.append(tz_path)
            continue

        title = view_title(tz_text, tz_path.parent.name)
        prompts.append((title, tz_path, prompt))

    return prompts, missing


def render_index(prompts: list[tuple[str, Path, str]]) -> str:
    lines = [
        "# Промти для візуалізації",
        "",
        "<!-- AUTO-GENERATED: редагуйте промпти у відповідних 00_Brief.md і запускайте scripts/update_visualization_prompts.py -->",
        "",
        "Цей файл автоматично збирається з розділів `## Промт для візуалізації` у ТЗ кожної архітектурної зони.",
        "Джерело правди: `01_Architectural_Zones/*/00_Brief.md`.",
        "",
    ]

    for title, tz_path, prompt in prompts:
        relative_tz = tz_path.relative_to(PROJECT_DIR)
        lines.extend(
            [
                f"## {title}",
                "",
                f"Джерело: `{relative_tz}`.",
                "",
                prompt,
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Update 04_Visualization_Prompts.md from TZ prompt sections."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate that every TZ has a prompt and the generated index is current.",
    )
    args = parser.parse_args()

    prompts, missing = collect_prompts()
    if missing:
        print("Missing prompt sections:", file=sys.stderr)
        for path in missing:
            print(f"- {path.relative_to(WORKSPACE_DIR)}", file=sys.stderr)
        return 1

    rendered = render_index(prompts)

    if args.check:
        current = read_text(OUTPUT_PATH) if OUTPUT_PATH.exists() else ""
        if current != rendered:
            print(f"{OUTPUT_PATH.relative_to(WORKSPACE_DIR)} is not up to date", file=sys.stderr)
            return 1
        print("Visualization prompt index is up to date.")
        return 0

    write_text(OUTPUT_PATH, rendered)
    print(f"Updated {OUTPUT_PATH.relative_to(WORKSPACE_DIR)} from {len(prompts)} TZ files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
