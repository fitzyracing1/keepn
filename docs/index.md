# keepn

`.keepn` is a declared text file type for append-only keep records. It is not an OS MIME registration. The repo also includes `SKILL.md`, a general "new file type" agent skill for defining `.kind` declarations with sample files.

## Format (README and `assets/keepn.kind`)

```
# keepn v1
---
title: example
kind: keepn
---
PROJECT: keepn
STATUS: public
```

- Line 1 must be `# keepn v1`. YAML frontmatter is optional.
- Body lines are `KEY: value`. Duplicate keys are appended, never overwritten.
- Values must not contain time words.

## Files
`assets/keepn.kind` (declaration), `SKILL.md`, the `ai-discovery/` pack (mirrored in `docs/ai-discovery/`), and the `docs/` site (https://fitzyracing1.github.io/keepn/, deployed by `pages.yml`).

The repo has no parser code and no LICENSE file. Copyright (c) 2026 Joshua Almeida
