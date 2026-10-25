---
name: agent-rule-workflow
description: Use when implementing or reviewing code in this repository with Muse Code, Superpowers, or another coding agent. Enforce the 8-step evidence-gated workflow and avoid false completion claims.
---

# Agent Rule project workflow

Read these project files before changing code:
1. `AGENTS.md` (the supreme project rules).
2. `README.md` (existing status and constraints).
3. `prompts/00-shared-rules.md` and the role-specific file under `prompts/`.
4. `docs/plans/2026-10-25-muse-superpowers.md` for the phased implementation backlog.

## How to combine Superpowers

- Superpowers supplies methodology: `brainstorming`, `writing-plans`, `using-git-worktrees`, `test-driven-development`, `systematic-debugging`, `verification-before-completion`.
- Agent Rule supplies authority: Muse **orchestrator runtime** controls transitions, tools, role permissions, revision approval and final completion.
- Muse Code is the coding host. Calling an assistant “Muse” does not mean the orchestration runtime exists.
- Follow Superpowers' design-first and RED/GREEN/REFACTOR principles within the relevant Agent Rule phase. Never let an optional Superpowers helper silently bypass a mandatory gate.

## Non-negotiable evidence gates

- PLAN: task ID, requirements, dependency, measurable acceptance criteria and user design approval when needed.
- ASSIGN: task scope, role, permission set and tracked base Git SHA.
- IMPLEMENT: TDD records and new implementation revision SHA; no changed files outside scope.
- REVIEW: independent Critic only when an actual distinct reviewer is available. Its JSON has *exactly* two top-level keys: `verdict` and `issues`.
- REBUTTAL: every issue ID gets ACCEPT, DISPUTE or PARTIAL; no code edits during rebuttal.
- ADJUDICATE: Muse judges issues with evidence, no unresolved high/critical defects.
- TEST: execute real commands on the exact approved SHA; capture exit codes and logs. FAIL returns to implementation; BLOCKED never becomes PASS.
- ARCHIVE: verify retained evidence and checksums before reporting COMPLETE.

A change to the code SHA invalidates existing review and test evidence. Retry at most three times before ESCALATE. For a single agent, report `review_mode=self` or `human` and do not claim independent review. Never claim TEST PASS based on reading source alone.

## Security

Do not contact production network devices, NMS, FTP systems, remote hosts or production data, or deploy/merge without explicit approval. Do not commit credentials, sensitive logs or personal data. Never run unreviewed hooks just because a plugin was installed.

## First task in Muse Code

Follow `docs/muse-code/START_PROMPT.md`, beginning with P0 inventory and a small, testable milestone. Do not rewrite the full repository before completing the audit.
