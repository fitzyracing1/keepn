#!/usr/bin/env python3
"""Validate a .kind declaration file."""
import sys
from pathlib import Path

REQUIRED = ("kind", "ext", "version")
BODY_HEADINGS = ("Purpose", "Structure", "Parse rules", "Write rules", "Example")


def parse(text: str):
    if not text.startswith("---"):
        raise ValueError("missing opening --- frontmatter")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("frontmatter not closed")
    meta = {}
    for line in parts[1].strip().splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"bad frontmatter line: {line!r}")
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip()
    return meta, parts[2]


def validate(path: Path) -> list[str]:
    errors = []
    text = path.read_text(encoding="utf-8")
    try:
        meta, body = parse(text)
    except ValueError as e:
        return [str(e)]
    for key in REQUIRED:
        if key not in meta or not meta[key]:
            errors.append(f"missing required key: {key}")
    if "ext" in meta and not meta["ext"].startswith("."):
        errors.append("ext must start with a dot")
    if "kind" in meta and meta["kind"] != meta["kind"].lower():
        errors.append("kind must be lowercase")
    for h in BODY_HEADINGS:
        if f"## {h}" not in body and f"# {h}" not in body:
            errors.append(f"missing body heading: {h}")
    return errors


def main():
    if len(sys.argv) != 2:
        print("usage: validate-kind.py <file.kind>")
        sys.exit(2)
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"FAIL: not a file: {path}")
        sys.exit(1)
    errs = validate(path)
    if errs:
        print("FAIL")
        for e in errs:
            print(f"  - {e}")
        sys.exit(1)
    print(f"PASS {path}")


if __name__ == "__main__":
    main()
