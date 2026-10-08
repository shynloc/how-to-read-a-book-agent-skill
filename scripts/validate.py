#!/usr/bin/env python3
"""Dependency-free structural checks for canonical and WorkBuddy Skills."""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / "skills" / "analytical-reading"
WORKBUDDY = ROOT / "platforms" / "workbuddy" / "analytical-reading"
REFERENCE_NAMES = (
    "READING-METHOD.md", "EVIDENCE-PROTOCOL.md",
    "GENRE-RULES.md", "REPORT-TEMPLATE.md",
)
VERSION = "2.1.0"


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        raise ValueError("unclosed YAML frontmatter")
    fields = {}
    # These manifests intentionally use only scalar top-level keys and a metadata map.
    for line in parts[0].splitlines()[1:]:
        if not line.strip() or line.startswith((" ", "\t")):
            continue
        match = re.fullmatch(r"([A-Za-z][A-Za-z_-]*):\s*(.*)", line)
        if not match:
            raise ValueError(f"unrecognized frontmatter line: {line!r}")
        key, value = match.groups()
        fields[key] = value.strip().strip('"').strip("'")
    return fields


def check() -> list[str]:
    errors = []
    for folder, workbuddy in ((CORE, False), (WORKBUDDY, True)):
        path = folder / "SKILL.md"
        if not path.is_file():
            errors.append(f"missing: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        try:
            fields = frontmatter(text)
        except ValueError as exc:
            errors.append(f"{path}: {exc}")
            continue
        name = fields.get("name", "")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or name != folder.name:
            errors.append(f"{path}: invalid name/directory mismatch")
        if not 1 <= len(fields.get("description", "")) <= 1024:
            errors.append(f"{path}: description required, <=1024 chars")
        expected = {"description_zh", "description_en", "version", "author"} if workbuddy else {"license", "metadata"}
        for key in expected:
            if key not in fields or (key != "metadata" and not fields[key]):
                errors.append(f"{path}: missing {key}")
        if workbuddy and fields.get("version") != VERSION:
            errors.append(f"{path}: version != {VERSION}")
        if not workbuddy and not re.search(r'(?m)^\s{2}version:\s*["\']?'+re.escape(VERSION), text):
            errors.append(f"{path}: metadata.version != {VERSION}")
        for name in REFERENCE_NAMES:
            resource = folder / "references" / name
            if not resource.is_file():
                errors.append(f"missing reference: {resource}")
            if (("@references/" if workbuddy else "references/") + name) not in text:
                errors.append(f"{path}: reference not linked: {name}")
        if workbuddy and not text.startswith("---\n"):
            errors.append("WorkBuddy parser requires frontmatter")
    for name in REFERENCE_NAMES:
        source = CORE / "references" / name
        clone = WORKBUDDY / "references" / name
        if source.exists() and clone.exists() and source.read_bytes() != clone.read_bytes():
            errors.append(f"WorkBuddy reference diverged from core: {name}")
    for required in ("README.md", "CHANGELOG.md", "LICENSE", "CONTRIBUTING.md",
                     "docs/PLATFORMS.md", "platforms/portable/PORTABLE-PROMPT.md",
                     "templates/READING-NOTE.md", "tests/BEHAVIOR-TESTS.md"):
        if not (ROOT / required).is_file():
            errors.append(f"missing project file: {required}")
    return errors


def main() -> int:
    errors = check()
    if errors:
        print("FAIL: Skill structural validation")
        for item in errors:
            print(" -", item)
        return 1
    print(f"PASS: canonical + WorkBuddy v{VERSION}; four mirrored references; required docs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
