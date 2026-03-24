---
name: wf-3-implement
description: >-
  Execute an implementation plan. Reads a plan file, creates a working branch, and guides through the development loop (TDD or implement-first). Use when implementing a planned feature or fix.
argument-hint: Path to a plan file (e.g., docs/workflow/plans/my-feature.md)
allowed-tools: Bash(git *) Bash(pytest *) Bash(python *) Bash(uv run *) Read Glob Grep Write Edit
disable-model-invocation: true
---

# Implement — Execute a Plan

Read a plan file and implement it.

## Context

- Current branch: !`git branch --show-current`
- Plan file: `$ARGUMENTS`
- Available plans: !`ls docs/workflow/plans/ 2>/dev/null || echo "(none)"`

## Steps

### 1. Read the Plan

If `$ARGUMENTS` is empty or not provided, list the available plan files in `docs/workflow/plans/` and ask the user which one to implement.

Otherwise, read the plan file at `$ARGUMENTS`. Extract:
- The approach (TDD or implement-first)
- The steps
- Files to create/modify
- Test strategy

### 2. Create a Working Branch

If not already on a feature branch, create one:

```bash
git checkout -b <branch-name-from-plan>
```

If already on a feature branch, confirm with the user before proceeding.

### 3. Execute the Development Loop

Follow the approach specified in the plan:

**If TDD:**
1. Write a failing test (pytest)
2. Write the minimum code to make it pass
3. Run `pytest` to verify
4. Refactor if needed
5. Repeat for each requirement

**If implement-first:**
1. Write the implementation code
2. Write tests to validate the implementation
3. Run `pytest` to verify
4. Iterate until all requirements are met

### 4. Update Documentation

Before finishing:
- Update the README if the feature adds user-facing functionality
- Update any relevant docs

### 5. Update Plan Status

Update the plan file's `status` frontmatter from `draft` to `implemented`.

### 6. Suggest Next Step

Tell the user implementation is complete and suggest they run `/wf-4-review` to review the changes before committing.
