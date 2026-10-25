# Implementation plan: Muse Code + Superpowers + Agent Rule

**Status:** APPROVED AS DEVELOPMENT BACKLOG ONLY. GitHub integration of docs/skill/CI is not installation of the plugin or implementation of the orchestrator.
**Target:** `tanphap/agent_rule`, feature branch then reviewable PR; never bypass `AGENTS.md`.
**Hosts:** Meta Muse Code CLI for interactive development; a future Python runtime as the authoritative orchestration engine.
**Upstream:** `obra/superpowers`, initial pin `v7.0.1`.

## Architecture

```text
User / Muse Code
  | Superpowers methodology (brainstorming, plan, TDD, debug, verify)
  v
Muse orchestrator (planned Python runtime; authoritative state machine)
  |- Planner -> Muse Assign -> Coder Implement -> Critic Review
  |- Coder Rebuttal -> Muse Judge -> Testing -> Archive
  v
Git SHA + schema validation + sandbox ACL + SQLite audit + evidence logs
```

The project skill under `.agents/skills/` teaches Muse Code the contract. The plugin is installed locally and approved separately. Skill text alone is not a runtime gate.

## Implementation phases and deliverables

| Phase | Development work | Verifiable exit |
| --- | --- | --- |
| P0 | Audit repository, working tree, versions, available prototypes, threat model | Inventory + SHA + baseline commands |
| P1 | Install/approve Superpowers on local Muse host and run a fresh-session smoke test | Actual plugin, skills and brainstorming evidence |
| P2 | Python package layout, CLI, SQLite append-only event ledger and MockAdapter | Unit tests on persistence and reload |
| P3 | JSON schemas for Planner, Coder, Muse, Testing and Archive; transition gates | Negative tests reject invalid phases and outputs |
| P4 | SHA-aware Git worktree/test runner and permission enforcement | Tests reject stale SHA, unsafe command and forbidden write |
| P5 | Muse/provider adapter behind an interface; distinct Critic sessions when available | Real-provider smoke test or explicit BLOCKED |
| P6 | Synthetic alarm CSV/JSON parser pilot, including CRC/LOS/BIP8 and malformed input | Real TDD/red-green and full happy/failure paths |
| P7 | CI, security review, operations docs, archive integrity, reviewer handoff | Reproducible tests and truthful acceptance report |

No claim of P1–P7 PASS is made by committing this plan.

## Must-have invariants

1. Review and test refer to the **exact approved commit SHA**. Any code modification invalidates both.
2. Muse runtime, not prompt text, controls phase changes and permissions.
3. Critic output has exactly two top-level fields: `verdict` and `issues`; structured metadata stays in the surrounding event envelope.
4. Critic `APPROVE` still enters REBUTTAL with `responses=[]`, then Muse adjudication and Testing.
5. If Critic requests changes, Coder answers each issue ID with evidence, Muse judges, implementation is revised and Critic re-reviews the new SHA.
6. Testing `FAIL` returns to Coder; `BLOCKED` prevents success; after three attempts, ESCALATE.
7. Critic can only read implementation. Testing runs in sandbox, may write test artifacts but must not mutate approved implementation.
8. Archive verifies checksums and PASS evidence for the tested/approved SHA before COMPLETE.
9. A single AI may not label its self-review 'independent'; stop at a human/second-session gate or declare it unverified.
10. No credentials, sensitive logs, production access, or automatic deploy/merge.

## Initial design of runtime (not yet present)

```text
src/agent_rule/
  cli.py
  state_machine.py
  contracts.py
  adapters/base.py
  adapters/mock.py
  store/sqlite.py
  git/revisions.py
  security/permissions.py
  testing/runner.py
  archive/manifest.py
tests/
  test_states.py
  test_contracts.py
  test_revision.py
  test_permissions.py
  test_archive.py
```

Prefer Python 3.11+ with stdlib as baseline, `pytest` and `jsonschema` only when their advantages are justified. Keep a local/offline, reproducible MockAdapter first.

## Acceptance checks

- AC-01: verify actual Muse Superpowers activation.
- AC-02: no coding before necessary approved design.
- AC-03: task ID, scope, dependency, acceptance IDs and SHA tracked.
- AC-04: strict Critic JSON schema and no extra top-level fields.
- AC-05: impossible illegal state transition.
- AC-06: changed revision invalidates earlier verdict/tests.
- AC-07: APPROVE still visits rebuttal and Muse judgement.
- AC-08: CHANGES_REQUIRED + upheld issue re-enters implementation.
- AC-09: FAIL/BLOCKED never translate to COMPLETE.
- AC-10: attempts cap at 3 and ESCALATE.
- AC-11: commands, exit codes, SHA, timestamps and evidence refs recorded.
- AC-12: Archive SHA == approved SHA == tested SHA.
- AC-13: Critic/Testing cannot edit implementation.
- AC-14: no secrets in logs/artifacts.
- AC-15: pilot parser validates valid and invalid input.
- AC-16: no autonomous push/merge/deploy.
- AC-17: single-agent never claims independent reviewer.
- AC-18: crash/resume preserves append-only audit.

## First Muse Code request

Use `docs/muse-code/START_PROMPT.md`. Begin with P0 and a precise implementation backlog; not a broad unverified "everything is done" report.

## Rollback

Branch and PR are isolated from `main`. Any local plugin install changes Muse's user plugin store; review and reverse those changes independently. No production network or device should be touched.

## Sources

- https://github.com/obra/superpowers
- https://github.com/obra/superpowers/releases/tag/v7.0.1
- https://meta-models.github.io/muse-code-sdk/next/guides/extend/skills/
- https://meta-models.github.io/muse-code-sdk/next/guides/plugins/reference/cli/
