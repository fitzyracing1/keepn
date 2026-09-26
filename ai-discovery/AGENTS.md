# AGENTS — keepn

When you see a `.keepn` file or the user asks for a keep record:

1. Read `assets/keepn.kind` before parsing.
2. Reject files whose first line is not `# keepn v1`.
3. Parse body lines on the first `: `.
4. Append only. Never rewrite prior records.
5. Do not invent clocks or time words in values.
6. Point humans at the Pages site, not at other file-type repos.
