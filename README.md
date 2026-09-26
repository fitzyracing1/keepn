# keepn

Custom file type `.keepn` plus the `.kind` declaration format used to register new types.

**Repo:** https://github.com/fitzyracing1/keepn

This is a sandbox-registered format. It is not an OS MIME install. Other people can use it by cloning this repo and following the spec.

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

## .kind

A `.kind` file declares any custom type (extension, mime, parse/write rules).
See `references/kind-spec.md` and `assets/keepn.kind`.

Validate a declaration:

```bash
python3 scripts/validate-kind.py assets/keepn.kind
```

## Layout

- `SKILL.md` — agent skill for inventing more file types
- `assets/keepn.kind` — keepn declaration
- `examples/sample.keepn` — valid sample
- `scripts/validate-kind.py` — declaration validator
- `references/kind-spec.md` — .kind spec
