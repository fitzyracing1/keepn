# keepn

Custom file type `.keepn` plus the `.kind` declaration format for this type.

**Repo:** https://github.com/fitzyracing1/keepn

This is a declared format. It is not an OS MIME install.

Sibling type: [hwlog](https://github.com/fitzyracing1/hwlog)

## .keepn

Text, append-only keep records.

```
# keepn v1
---
title: example
kind: keepn
---
PROJECT: keepn
STATUS: public
```

Rules:
- Line 1 must be `# keepn v1`
- Optional YAML frontmatter
- Body lines are `KEY: value`
- Duplicate keys append; do not overwrite
- No time words in values

## Validate

```bash
python3 scripts/validate-kind.py assets/keepn.kind
```

## Layout

- `assets/keepn.kind` — keepn declaration
- `examples/sample.keepn` — valid sample
- `scripts/validate-kind.py` — declaration validator
- `references/kind-spec.md` — .kind spec
- `SKILL.md` — agent skill for inventing more file types (each type ships in its own repo)
