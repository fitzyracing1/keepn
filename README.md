# keepn

Custom file types plus the `.kind` declaration format used to register new types.

**Repo:** https://github.com/fitzyracing1/keepn

This is a declared format. It is not an OS MIME install. Clone the repo to use it.

## Types

| Kind | Ext | Banner | Use |
|---|---|---|---|
| keepn | `.keepn` | `# keepn v1` | append-only keep records |
| hwlog | `.hwlog` | `# hwlog v1` | hardware prototype log |

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

## .hwlog

Append-only hardware prototype log. One ENTRY block per update. Phone dictation maps onto STATUS, PROGRESS, PART, BOM, BLOCKER, NEXT.

```
# hwlog v1
---
PROJECT: Tesla Bot Cruiser
RIG: garage bay
---
ENTRY: 1
STATUS: Prototyping
PROGRESS: 12
PART: modular hull panel A
BOM: interlocking edge clips x8
NEXT: dry-fit panel A to rail
```

Rules:
- Line 1 must be `# hwlog v1`
- Frontmatter must include PROJECT
- Entries are numbered; append only
- STATUS is one of Concept, Design, Prototyping, Testing, Production Ready, Complete, On Hold
- PROGRESS is 0-100

See `assets/hwlog.kind` and `examples/sample.hwlog`.

## .kind

A `.kind` file declares any custom type (extension, mime, parse/write rules).
See `references/kind-spec.md`.

Validate a declaration:

```bash
python3 scripts/validate-kind.py assets/hwlog.kind
```

## Layout

- `SKILL.md` — agent skill for inventing more file types
- `assets/keepn.kind` — keepn declaration
- `assets/hwlog.kind` — hardware log declaration
- `examples/sample.keepn` — keepn sample
- `examples/sample.hwlog` — hardware log sample
- `scripts/validate-kind.py` — declaration validator
- `references/kind-spec.md` — .kind spec
