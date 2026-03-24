"""Tests for the local workflow skills (wf-1 through wf-4)."""

import re
from pathlib import Path

import yaml
import pytest

SKILLS_DIR = Path(__file__).parent.parent / ".claude" / "skills"
WORKFLOW_SKILLS = ["wf-1-ideate", "wf-2-plan", "wf-3-implement", "wf-4-review"]


def _parse_frontmatter(path: Path) -> dict:
    """Extract YAML frontmatter from a SKILL.md file."""
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    assert match, f"No frontmatter found in {path}"
    return yaml.safe_load(match.group(1))


@pytest.mark.parametrize("skill_name", WORKFLOW_SKILLS)
class TestSkillStructure:
    """Verify each skill has valid structure and frontmatter."""

    def test_skill_file_exists(self, skill_name):
        path = SKILLS_DIR / skill_name / "SKILL.md"
        assert path.exists(), f"{path} does not exist"

    def test_frontmatter_has_required_fields(self, skill_name):
        path = SKILLS_DIR / skill_name / "SKILL.md"
        fm = _parse_frontmatter(path)
        for field in ("name", "description", "allowed-tools"):
            assert field in fm, f"Missing '{field}' in {skill_name} frontmatter"

    def test_name_matches_directory(self, skill_name):
        path = SKILLS_DIR / skill_name / "SKILL.md"
        fm = _parse_frontmatter(path)
        assert fm["name"] == skill_name

    def test_no_gh_cli_references(self, skill_name):
        path = SKILLS_DIR / skill_name / "SKILL.md"
        content = path.read_text(encoding="utf-8")
        assert "gh issue" not in content, f"{skill_name} references 'gh issue'"
        assert "gh pr" not in content, f"{skill_name} references 'gh pr'"
        assert "gh api" not in content, f"{skill_name} references 'gh api'"

    def test_no_gh_in_allowed_tools(self, skill_name):
        path = SKILLS_DIR / skill_name / "SKILL.md"
        fm = _parse_frontmatter(path)
        tools = fm["allowed-tools"]
        assert "gh " not in tools, f"{skill_name} has gh CLI in allowed-tools"


class TestWorkflowOutputPaths:
    """Verify skills reference the correct output directories."""

    def test_ideate_outputs_to_ideas(self):
        path = SKILLS_DIR / "wf-1-ideate" / "SKILL.md"
        content = path.read_text(encoding="utf-8")
        assert "docs/workflow/ideas/" in content

    def test_plan_outputs_to_plans(self):
        path = SKILLS_DIR / "wf-2-plan" / "SKILL.md"
        content = path.read_text(encoding="utf-8")
        assert "docs/workflow/plans/" in content

    def test_review_outputs_to_reviews(self):
        path = SKILLS_DIR / "wf-4-review" / "SKILL.md"
        content = path.read_text(encoding="utf-8")
        assert "docs/workflow/reviews/" in content


class TestWorkflowDirectories:
    """Verify the workflow storage directories exist."""

    @pytest.mark.parametrize("subdir", ["ideas", "plans", "reviews"])
    def test_directory_exists(self, subdir):
        path = Path(__file__).parent.parent / "docs" / "workflow" / subdir
        assert path.is_dir(), f"docs/workflow/{subdir}/ does not exist"
