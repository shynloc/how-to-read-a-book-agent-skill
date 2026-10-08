#!/usr/bin/env python3
"""Explicitly synchronize shared reference documents to WorkBuddy package."""
from pathlib import Path
from shutil import copy2
from validate import CORE, WORKBUDDY, REFERENCE_NAMES

def main():
    target = WORKBUDDY / "references"
    target.mkdir(parents=True, exist_ok=True)
    for name in REFERENCE_NAMES:
        copy2(CORE / "references" / name, target / name)
        print("synced:", name)

if __name__ == "__main__":
    main()
