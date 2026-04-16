# Facts

> Compact confirmed facts for the SAMPLE_PROJECT support desk example.

## Project

- The sample is a pedagogical CLI app, not a production template.
- It uses Python standard library only.
- It has no frontend, production database, hosting or external integrations.
- GitHub and Markdown are the approved documentation/versioning base.

## Runtime Data

- `data/requests.json` is local runtime persistence only.
- `src/` contains the minimum automation aligned with OpenSpec.
- `graphify-out/` contains derived structural context.

## Current Issues

| Issue | Impact | Mitigation |
|---|---|---|
| Graphify may not be installed locally. | Derived context can become stale. | Regenerate when available; otherwise treat output as stale. |
| The sample can be mistaken for a production base. | Scope creep. | Check `PROJECT_GUIDE.md` and `docs/architecture/system.md` before expanding. |
| Manual priority choices can vary. | Inconsistent operations. | Keep functional policy in OpenSpec and patterns in memory. |
