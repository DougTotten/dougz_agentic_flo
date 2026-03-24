---
name: wf-4-review
description: >-
  Review changes on the current branch before committing. Analyzes code for bugs, performance, security, and correctness issues. Writes findings to a local markdown file. Use when reviewing code, checking quality, or as a pre-commit gate.
argument-hint: "[base-branch] (defaults to main or master)"
allowed-tools: Bash(git *) Read Glob Grep Write
disable-model-invocation: true
---

# Review — Pre-Commit Code Review

Analyze changes on the current branch and write a review before committing.

> Based on [Jose Casanova's PR review prompt](https://www.josecasanova.com/prompts/git-concise-pr-review-prompt).

## Context

- Current branch: !`git branch --show-current`
- Base branch: !`git log --oneline --all --graph -10`
- Changed files: !`git diff --stat $(git merge-base HEAD main 2>/dev/null || git merge-base HEAD master 2>/dev/null || echo HEAD~5)..HEAD`

## Steps

### 1. Determine Base Branch

Use `$ARGUMENTS` as the base branch if provided. Otherwise, detect the default branch (`main` or `master`).

### 2. Analyze Changes

Run `git diff <base>..HEAD` to get the full diff. Also review any unstaged or staged changes with `git diff` and `git diff --cached`.

Focus **only** on critical issues:

- **Bugs** — logic errors, edge cases, race conditions, off-by-one errors
- **Performance** — inefficient algorithms, unnecessary loops, memory issues, large data copies
- **Security** — injection, exposure, auth gaps, unsafe deserialization
- **Correctness** — does the code do what it claims? Are tests actually testing the right things?

For Python/ML code, also watch for:
- Numpy/pandas anti-patterns (iterating instead of vectorizing)
- Missing input validation on data shapes/types
- Unreproducible randomness (missing seeds)
- Silent failures in data pipelines

### 3. Write the Review

Create a review file at `docs/workflow/reviews/<branch-name>.md`:

```markdown
---
title: Review — <branch-name>
date: <YYYY-MM-DD>
branch: <branch-name>
base: <base-branch>
verdict: approved | issues-found
---

## Summary

<1-2 sentence summary of what the changes do>

## Findings

<If critical issues found: list as bullet points with file:line references>
<If no critical issues: "No critical issues found.">

## Verdict

<approved or issues-found with emoji: approved or warning>
<Model name>
```

Skip style suggestions and minor nitpicks unless they impact performance, security, or correctness.

### 4. Present Results

Show the review to the user. If approved, suggest committing. If issues were found, list them and ask how the user wants to proceed.
