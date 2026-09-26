# .kind specification

A `.kind` file declares a custom file type.

## Frontmatter

```
---
kind: keepn
ext: .keepn
version: 1
mime: application/x-keepn
binary: false
trigger: keepn keep record
---
```

- kind: kebab-case, lowercase
- ext: must start with `.`
- version: integer or semver
- mime: defaults to application/x-<kind>
- binary: defaults false
- trigger: optional words

## Body headings (required)

## Purpose
## Structure
## Parse rules
## Write rules
## Example
