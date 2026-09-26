# keepn

Custom file type `.keepn`.

**Repo:** https://github.com/fitzyracing1/keepn  
**Pages:** https://fitzyracing1.github.io/keepn/  
**AI discovery pack:** https://fitzyracing1.github.io/keepn/ai-discovery/

Declared format. Not an OS MIME install.

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

## Pages

Site source is `docs/`. If the live URL 404s, enable Pages once:

GitHub repo → Settings → Pages → Source: GitHub Actions

## AI discovery pack

Machine-readable pack for agents:

- `ai-discovery/pack.json`
- `ai-discovery/llms.txt`
- `ai-discovery/AGENTS.md`
- `ai-discovery/SKILL.md`

Validate the type declaration:

```bash
python3 scripts/validate-kind.py assets/keepn.kind
```
