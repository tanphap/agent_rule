# Muse Code + Superpowers: setup and verification

This guide targets **Meta Muse Code CLI** (`muse`), **not** the unrelated video service formerly named muse.ai (now Skiv).

Repository: https://github.com/tanphap/agent_rule
Upstream Superpowers: https://github.com/obra/superpowers
Initial pinned release for reproducibility: `v7.0.1` (verify the release before upgrading).

## 1. Open a local workspace

```bash
git clone https://github.com/tanphap/agent_rule.git
cd agent_rule
git switch feat/muse-code-superpowers-bootstrap-20261025
git status --short
git rev-parse HEAD
muse --version
```

If the feature branch has already been merged, use `main` instead. Do not overwrite a dirty working tree.

## 2. Inspect and install upstream Superpowers locally

The plugin is a **local Muse installation**, not a GitHub setting. Do not copy Superpowers' entire repository into `agent_rule`.

```bash
git clone --depth 1 --branch v7.0.1 https://github.com/obra/superpowers.git ../superpowers
muse plugins validate ../superpowers
muse plugins install ../superpowers
muse plugins inspect superpowers
```

Review the hook command definitions and permissions before approving. If trusted:

```bash
muse plugins approve superpowers
muse plugins list
```

Muse requires approval of hooks and other runtime capabilities. Restart Muse after approval for the native SessionStart bootstrap to be active.

## 3. Verify actual skill activation

```bash
muse skills list --source plugin
muse skills list --source project --trust-workspace
muse skills validate .agents/skills/agent-rule-workflow
```

The project skill is committed under `.agents/skills/agent-rule-workflow/SKILL.md`. Project skills load only in a trusted workspace; review source before trusting it.

Start a fresh Muse session, ask for a small new feature, and confirm that brainstorming occurs **before** code changes. Then ask Muse to read `AGENTS.md` and `docs/muse-code/START_PROMPT.md`. Save actual command outputs and session evidence in a non-secret local path.

## 4. Development handoff

In Muse Code, paste the instructions from `docs/muse-code/START_PROMPT.md`. First milestone is P0 (inventory); subsequent milestones are P1-P7 in `docs/plans/2026-10-25-muse-superpowers.md`.

Muse Code and the Muse orchestrator are distinct:
- Muse Code is a coding environment/agent.
- The project-specific Muse orchestrator is software to be implemented; prompt files alone do not enforce tool ACL, state transitions, or Git SHA gates.

Until the runtime and independent reviewer exist, say `MOCK` / `NOT_RUN` / `BLOCKED` rather than claiming a complete multi-agent pipeline.

## 5. Troubleshooting / rollback

- If `muse plugins` is unavailable, record the Muse version and consult its CLI documentation; do not improvise unsupported commands.
- If a skill is missing, confirm plugin installation/approval, restart, workspace trust, and `muse skills list` diagnostics.
- Upstream updates: inspect release notes; then `muse plugins update superpowers` if supported by your Muse version.
- To back out of this GitHub integration, close the PR or delete its unmerged feature branch. Local plugin removal requires verification of the host-specific command; do not silently change user settings.

## Sources

- https://github.com/obra/superpowers#installation
- https://meta-models.github.io/muse-code-sdk/next/guides/plugins/reference/cli/
- https://meta-models.github.io/muse-code-sdk/next/guides/extend/skills/
