---
name: wf-2-plan
description: >-
  Plan implementation for a local idea file. Reads the idea, researches official docs, and produces a development plan. Defaults to TDD but supports opting out. Use when planning work or preparing an implementation.
argument-hint: Path to an idea file (e.g., docs/workflow/ideas/my-feature.md)
allowed-tools: Read Glob Grep WebFetch Write
disable-model-invocation: true
---

# Plan — Plan Implementation from an Idea

Read a local idea file and produce a development plan.

## Context

- Current branch: !`git branch --show-current`
- Idea file: `$ARGUMENTS`
- Available ideas: !`ls docs/workflow/ideas/ 2>/dev/null || echo "(none)"`

## Steps

### 1. Read the Idea

If `$ARGUMENTS` is empty or not provided, list the available idea files in `docs/workflow/ideas/` and ask the user which one to plan.

Otherwise, read the idea file at `$ARGUMENTS`. Identify:
- The goal and expected outcome
- Technical requirements
- Potential challenges

### 2. Research

If needed, research using **official documentation only** (not blog posts or unofficial GitHub repos).

Use `WebFetch` to pull official docs when needed.

### 3. Raise Doubts

Point out any doubts about the implementation. **Only continue if you are confident about the approach.** If unsure, explain what's unclear and use the AskUserTool to ask questions.

### 4. Assess TDD Fit

Consider whether test-driven development is appropriate for this work:

- **TDD is a good fit** when: behavior is well-defined, inputs/outputs are clear, working with data transformations, building APIs or utilities.
- **TDD is a poor fit** when: exploring an algorithm whose output is unknown, prototyping signal processing pipelines, doing exploratory data analysis, or when the correct result can only be judged visually or empirically.

If TDD does not fit, **recommend opting out** and explain why. Ask the user to confirm the approach.

### 5. Create the Plan

Write the plan to `docs/workflow/plans/<slug>.md` where `<slug>` matches the idea file name.

The plan file must follow this structure:

```markdown
---
title: <plan title>
date: <YYYY-MM-DD>
idea: <path to idea file>
approach: tdd | implement-first
status: draft
---

## Goal

<What we're building and why>

## Approach

<TDD or implement-first, with justification>

## Steps

1. **Create a working branch**: `git checkout -b <descriptive-slug>`
2. <If TDD>: **Write tests first** (pytest), then write code to make them pass
   <If implement-first>: **Write code first**, then write tests to validate
3. **Run tests** to verify: `pytest <test-path>`
4. **Repeat** until all requirements are met
5. **Update documentation** — README and any relevant docs

## Files to Create/Modify

<List of files that will be created or changed>

## Test Strategy

<What to test and how — pytest fixtures, parametrize, etc.>

## Open Questions

<Anything unresolved>
```

### 6. Present Options

Ask the user:

- **"Clear context and execute"** — start a fresh session and run `/wf-3-implement docs/workflow/plans/<slug>.md`
- **"Save plan for later"** — plan is already saved, just confirm the path
