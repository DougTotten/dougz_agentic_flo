# Workflow

This directory stores artifacts produced by the `wf-*` Claude Code skills. Each subdirectory corresponds to a stage of the local development workflow.

## Directory Structure

```
docs/workflow/
├── ideas/       # Captured ideas and problem descriptions
├── plans/       # Implementation plans derived from ideas
└── reviews/     # Pre-commit code reviews
```

## Workflow Stages

| Stage | Skill | What it does |
|-------|-------|-------------|
| 1. Ideate | `/wf-1-ideate <your idea>` | Captures an idea as a structured markdown file |
| 2. Plan | `/wf-2-plan <idea-file>` | Produces an implementation plan (TDD or implement-first) |
| 3. Implement | `/wf-3-implement <plan-file>` | Executes the plan — creates branch, writes code and tests |
| 4. Review | `/wf-4-review [base-branch]` | Reviews changes before committing |

## File Formats

All workflow files use markdown with YAML frontmatter. Each file includes:
- `title` — descriptive name
- `date` — creation date (YYYY-MM-DD)
- `status` — current state (e.g., `open`, `draft`, `implemented`, `approved`)

## Usage

```bash
# Start with an idea
/wf-1-ideate Add a Kalman filter for sensor fusion

# Plan the implementation
/wf-2-plan docs/workflow/ideas/kalman-filter-sensor-fusion.md

# Implement the plan
/wf-3-implement docs/workflow/plans/kalman-filter-sensor-fusion.md

# Review before committing
/wf-4-review
```
