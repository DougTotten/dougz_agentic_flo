# dougz_agentic_flo

Local-first development workflow skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). Designed for Python teams working on algorithm design, ML, deep learning, and signal processing.

## Workflow

| Stage | Command | Output |
|-------|---------|--------|
| 1. Ideate | `/wf-1-ideate <idea>` | `docs/workflow/ideas/<slug>.md` |
| 2. Plan | `/wf-2-plan <idea-file>` | `docs/workflow/plans/<slug>.md` |
| 3. Implement | `/wf-3-implement <plan-file>` | Code + tests on a feature branch |
| 4. Review | `/wf-4-review` | `docs/workflow/reviews/<branch>.md` |

All workflow artifacts are stored as local markdown files in `docs/workflow/` — no GitHub issues or PRs required.

## Multi-agent orchestration

For non-trivial migrations where context-rot or model cost is a concern, use `/delegated-build` to run the workflow with model right-sizing: Opus orchestrates from the main thread, Sonnet subagents run the wf-1/wf-2/wf-3 chain, and Haiku handles mechanical edits inside wf-3. Every subagent invocation is traced in a live mermaid sequence diagram (`docs/workflow/<active-workflow>/agent-trace.md`) recording why/model/tokens for each call.

See [.claude/skills/delegated-build/SKILL.md](.claude/skills/delegated-build/SKILL.md) for the full protocol.

## Setup

1. Clone this repo into your project (or copy the `.claude/skills/` directory)
2. Install dev dependencies for tests:

```bash
uv sync
```

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

## Testing

```bash
uv run pytest
```

## Details

See [docs/workflow/README.md](docs/workflow/README.md) for the full workflow documentation.
