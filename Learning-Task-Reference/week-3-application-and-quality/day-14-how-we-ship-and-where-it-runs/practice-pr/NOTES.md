# Practice PR

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 14: How we ship, and where it runs** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** Changes reach main through a branch, a PR with the template, automatic checks, and a human review.

**How does it work?** branch > commit > ./scripts/format.sh > ./scripts/validate.sh > push > PR (template) > CI > review > merge

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- What does CI run?
- What does validate.sh catch that your tests do not?

## What to do
1. Branch from your learning branch; run ./scripts/format.sh and ./scripts/validate.sh
2. Open a PR using the template; buddy reviews; address comments

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `.github/pull_request_template.md`
- `scripts/format.sh`
- `scripts/validate.sh`
- `.github/workflows/ci.yml`

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
