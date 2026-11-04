# clean.issue

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 17: Capstone 2: raw table and clean view** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** Clean is a view over raw that keeps only the latest version of each issue, typed. A view stays correct whenever raw changes.

**How does it work?** raw rows > rank by updated_at per issue > keep latest > cast types > view

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- Why a view and not a copy?
- How do you break ties?

## What to do
1. One row per issue, latest version, typed: number, title, state, labels, created at, closed at, updated at
2. Tie-breaker for equal updated_at

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `product/egpt_retail/warehouse/sql/conform/crm_deal.sql`

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.
- `clean_issue.sql`

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
