# Agent Rule — Multi-Agent Engineering Pipeline (8 steps)

An evidence-gated workflow for Planner → Muse → Coder → Critic → Coder Rebuttal → Muse Judge → Testing → Archive.

## Develop with Meta Muse Code + Superpowers

This repository can now be opened in Muse Code as a **project skill** workspace. The Superpowers plugin is installed and approved separately on the Muse host; GitHub commits do not install it.

- [Muse Code setup and verification](docs/muse-code/SETUP.md)
- [Copy-ready Muse development prompt](docs/muse-code/START_PROMPT.md)
- [Phased runtime implementation plan](docs/plans/2026-10-25-muse-superpowers.md)
- [Project skill](.agents/skills/agent-rule-workflow/SKILL.md)

Run the repository's **static contract checks** with `python -m unittest discover -s tests -p "test_repository_contracts.py" -v`. These checks verify source contracts only: they do **not** execute the 8-step runtime or certify any multi-agent deployment.

## Important
This repository contains **agent system prompts and workflow contracts**. Merely installing prompts does **not** automatically connect GPT/Codex, Gemini, Muse or Antigravity. The external runner must call agents, validate JSON, preserve commit SHA, enforce tool permissions and store logs.

## Pipeline
1. Planner: produce testable tasks.
2. Muse Leader: assign tasks and dependencies.
3. Coder: implement on a tracked revision.
4. Critic: independent verdict and issues JSON.
5. Coder: address each issue with evidence or concede.
6. Muse: adjudicate each issue and approve/rework.
7. Testing (target model `cx/gpt-5.6-sol`): actual test execution, PASS/FAIL/BLOCKED; FAIL loops to step 3.
8. Archivist: commit SHA, decisions, logs and PASS evidence.

Muse orchestrates all gates. A changed revision invalidates previous review/tests. Limit retries to 3; escalate thereafter.

## Prompt files
- [Shared law](prompts/00-shared-rules.md)
- [Planner](prompts/01-planner.md)
- [Muse](prompts/02-muse.md)
- [Coder](prompts/03-coder.md)
- [Critic](prompts/04-critic.md)
- [Testing](prompts/05-testing.md)
- [Archivist](prompts/06-archivist.md)

## Usage in Antigravity or an agent manager
Set each agent's **System Prompt** to the content of its corresponding file plus shared rules. Do **not** paste a file's prompt into user requests. Configure model, working directory and tool permissions in the agent host. Keep Critic read-only; Testing runs on sandbox staging, not production.

## Runtime integration checklist
- Parser validates Critic `{"verdict","issues"}` and other step schemas.
- Gates check `task_id`, `attempt`, exact `revision` and evidence.
- Muse stores state and prevents illegal transitions.
- Every retry creates new revision, re-reviews changes.
- Testing records actual exit codes, command and evidence paths.
- Archive verifies PASS of approved SHA before COMPLETE.
- No API keys, production network credentials or sensitive logs committed.

## Status
This initial GitHub import provides the role instructions and contracts. It is **not** a deployed live 6-agent service. See local package previously supplied in the chat for prototype CLI/SQLite engine.
