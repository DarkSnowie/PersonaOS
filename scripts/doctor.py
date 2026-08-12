#!/usr/bin/env python3

import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def check(title, ok):
    icon = "✓" if ok else "✗"
    print(f"{icon} {title}")


print("PersonaOS Development Environment")
print("=" * 40)

check("Python", sys.version_info >= (3, 12))
check("Git", shutil.which("git") is not None)
check("uv", shutil.which("uv") is not None)
check("Ruff", shutil.which("ruff") is not None)

print()

print("Project Files")
print("=" * 40)

required = [
    "pyproject.toml",
    ".editorconfig",
    ".gitignore",
    ".envrc",
    "CLAUDE.md",
]

for file in required:
    check(file, (ROOT / file).exists())

print()

print("Git Status")
print("=" * 40)

try:
    subprocess.run(
        ["git", "status", "--short"],
        cwd=ROOT,
        check=False,
    )
except Exception:
    print("Unable to read git status.")
