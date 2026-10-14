# Integration roadmap

**Current state:** Prompts, JSON schemas and design rules only in this PR. The companion local starter kit includes a manual-submission SQLite engine; this repository has not yet been wired to cloud AI APIs or to an unattended scheduler.

1. Import each `prompts/NN-*.md` with `prompts/00-shared-rules.md` into the matching agent System Prompt configuration.
2. Configure actual model IDs in your gateway: Coder as provisioned; Testing requested `cx/gpt-5.6-sol`; Gemini Reviewer when available. Model name in a prompt alone does not switch provider.
3. Provide repository worktrees and exact Git commit SHA; enforce least-privilege execution in the host.
4. Add adapters to invoke agents with Task Envelope and parse outputs with schemas.
5. Persist state in SQLite/PostgreSQL with serialized transitions to avoid double-submit/races.
6. Integrate CI testing via GitHub Actions/check-runs. Validate successful job/commit SHA and store logs.
7. Archive immutable artifacts, SHA256 manifest and audit events.
8. Only after authenticated adapters and validations are operational enable Muse-controlled unattended dispatch.

**Muse / Antigravity caveat:** whether one service can invoke another is dependent on provider-supported API, connector or permitted plugin integration. Do not scrape login sessions or repurpose personal authentication tokens.

## Human-in-the-loop
Require human approval for production deployments, infrastructure changes, credential/permission updates, high-cost actions and changes to acceptance criteria.

## Manual fallback
Without official API integration: operator invokes each agent, deposits its JSON output into a shared workspace, the state machine validates before advancing. This is an auditable starter, not full automation.
