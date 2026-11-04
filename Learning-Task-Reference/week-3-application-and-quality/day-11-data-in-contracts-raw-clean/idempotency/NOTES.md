# Idempotency and watermark

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 11: Data in: contracts, raw and clean** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** An operation is idempotent if running it twice leaves the same result as running it once. Loads and pulls must be.

**How does it work?** load file > key (file path, line number) already seen? yes: skip; no: insert

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- Where in the code is the duplicate prevented?
- Why must the watermark move only after the write succeeds?

## What to do
1. Show in code where a second load of the same file is prevented
2. Explain why the watermark moves only after a successful write

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `product/egpt_retail/contracts/LANDING_CONTRACT.md` — 'Re-run behaviour'
- `product/egpt_retail/warehouse/LOAD_CONTRACT.md` — 'When a load does not finish'

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
