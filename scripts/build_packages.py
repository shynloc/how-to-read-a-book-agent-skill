#!/usr/bin/env python3
"""Build standalone portable and WorkBuddy ZIPs without third-party dependencies."""
from __future__ import annotations
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from validate import ROOT, CORE, WORKBUDDY, VERSION, check


def pack(folder: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output, "w", ZIP_DEFLATED, compresslevel=9) as archive:
        for source in sorted(folder.rglob("*")):
            if source.is_file() and not source.name.startswith("."):
                # A single top-level skill directory, matching YAML 'name'.
                path_in_zip = Path("analytical-reading") / source.relative_to(folder)
                archive.write(source, path_in_zip.as_posix())
    print("built:", output)


def main() -> int:
    issues = check()
    if issues:
        for issue in issues:
            print("FAIL:", issue)
        return 1
    dist = ROOT / "dist"
    pack(CORE, dist / f"analytical-reading-agent-skill-v{VERSION}.zip")
    pack(WORKBUDDY, dist / f"workbuddy-analytical-reading-v{VERSION}.zip")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
