---
name: new-file-type
description: Activate when the user wants to invent, register, or use a custom file type. Handles .kind declarations, sample files, validators, MIME-style names, and parse/write rules. Triggers include create a new file type, new extension, custom file format, .kind file, register file type, invent a format.
---

# New File Type

## Overview

Define a custom file type as a `.kind` declaration plus at least one sample file. A kind is a named format with an extension, optional MIME, version, and parse/write rules the agent must follow whenever that type appears.

## Format of a `.kind` file

Plain text. YAML frontmatter, then a markdown body.

Required frontmatter keys:

- kind — short kebab-case name of the type
- ext — extension including the leading dot (example .keepn)
- version — integer or semver string

Optional:

- mime — application/x-<kind> if omitted
- binary — true only if the payload is not text
- trigger — words that should load this kind later

Body sections (use these headings):

- Purpose
- Structure
- Parse rules
- Write rules
- Example

## Instructions

1. When the user says create a new file type without naming it, invent a short kind name from the current project context. Default kind name is keepn and default extension is .keepn if nothing else fits.
2. Write three artifacts every time:
   - `assets/<kind>.kind` — the declaration
   - `examples/sample.<ext-without-dot>` — a valid sample of the new type
   - a one-page human note in README or examples/
3. Keep the payload text unless the user explicitly asks for binary.
4. After writing, run `scripts/validate-kind.py` on the `.kind` file and report pass/fail.
5. In the reply, state the kind name, extension, mime, and where the files live. Do not dump the whole spec unless asked.
6. Later sessions that see a matching extension must read the `.kind` file first, then treat the payload by those parse rules.

## Default type if unspecified

If the user gives no name, register **keepn** (`.keepn`):

- Text file
- First line `# keepn v1`
- Then optional YAML frontmatter between `---` lines
- Then a body of short records, one per line, each `KEY: value`
- No time words in the body
- Used as an append-only keep record for Access-style archives and project notes

## Constraints

- Do not overwrite an existing `.kind` of the same name. Version-bump instead.
- Do not invent binary encodings unless asked.
- Do not claim OS-level MIME registration. This type exists as a declared format in this repo and in the skill.
