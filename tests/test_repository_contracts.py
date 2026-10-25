"""Static baseline checks; these do not claim the future orchestrator is running."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RepositoryContractTests(unittest.TestCase):
    def test_critic_schema_requires_exact_two_top_level_keys(self):
        schema = json.loads((ROOT / "schemas/critic.schema.json").read_text(encoding="utf-8"))
        self.assertEqual(set(schema["required"]), {"verdict", "issues"})
        self.assertFalse(schema["additionalProperties"])
        self.assertEqual(
            set(schema["properties"]["verdict"]["enum"]),
            {"APPROVE", "CHANGES_REQUIRED", "BLOCKED"},
        )

    def test_role_prompts_exist(self):
        for filename in (
            "00-shared-rules.md",
            "01-planner.md",
            "02-muse.md",
            "03-coder.md",
            "04-critic.md",
            "05-testing.md",
            "06-archivist.md",
        ):
            with self.subTest(filename=filename):
                self.assertTrue((ROOT / "prompts" / filename).is_file())

    def test_muse_project_skill_contract(self):
        skill = (ROOT / ".agents/skills/agent-rule-workflow/SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(skill.startswith("---\n"))
        self.assertIn("name: agent-rule-workflow", skill)
        self.assertIn("description:", skill)
        self.assertIn("AGENTS.md", skill)
        self.assertIn("review_mode=self", skill)

    def test_handoff_and_plan_exist(self):
        for path in (
            "docs/muse-code/SETUP.md",
            "docs/muse-code/START_PROMPT.md",
            "docs/plans/2026-10-25-muse-superpowers.md",
        ):
            with self.subTest(path=path):
                self.assertGreater((ROOT / path).stat().st_size, 100)
        plan = (ROOT / "docs/plans/2026-10-25-muse-superpowers.md").read_text(encoding="utf-8")
        for phase in range(8):
            self.assertIn(f"P{phase}", plan)
        for criterion in range(1, 19):
            self.assertIn(f"AC-{criterion:02}", plan)


if __name__ == "__main__":
    unittest.main()
