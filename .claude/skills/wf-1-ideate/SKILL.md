---
name: wf-1-ideate
description: >-
  Capture an idea or problem as a structured local markdown file. Asks clarifying questions, researches official docs, and writes to docs/workflow/ideas/. Use when starting new work, reporting a bug, or capturing an idea.
argument-hint: Your idea or problem description
allowed-tools: Read Glob Grep WebFetch Write
disable-model-invocation: true
---

# Ideate — Capture an Idea

Turn an idea or problem into a well-structured markdown file.

## Context

- Current branch: !`git branch --show-current`
- Recent commits: !`git log --oneline -5`
- Existing ideas: !`ls docs/workflow/ideas/ 2>/dev/null || echo "(none yet)"`

## The Idea

$ARGUMENTS

## Steps

### 1. Clarify

Ask the user clarifying questions about the idea before writing anything. Use the AskUserTool. Understand:
- What problem does this solve?
- What should the end result look like?
- Are there constraints or preferences?

### 2. Research

If the idea involves packages, APIs, or frameworks, look up **official documentation only** (not blog posts or unofficial GitHub repos).

Use `WebFetch` to pull official docs when needed.

### 3. Write the Idea File

Create a markdown file at `docs/workflow/ideas/<slug>.md` where `<slug>` is a short, descriptive kebab-case name derived from the idea.

The file must follow this structure:

```markdown
---
title: <clear, descriptive title>
date: <YYYY-MM-DD>
status: open
---

## Problem

<What problem does this solve? Why does it matter?>

## Desired Outcome

<What should the end result look like?>

## Constraints

<Any constraints, preferences, or requirements>

## Implementation Suggestions

<High-level suggestions — not a full plan>

## References

<Links to official docs, if any>
```

**Do NOT plan the implementation.** The goal is a well-written idea file that can be picked up later with `/wf-2-plan`.

### 4. Confirm

Tell the user the file was created and suggest they run `/wf-2-plan docs/workflow/ideas/<slug>.md` when ready to plan the implementation.
