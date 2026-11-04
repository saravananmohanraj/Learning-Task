# Watermark in Postgres

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 16: Capstone 1: pull and land files** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** A watermark remembers 'pulled up to here' so each run fetches only what changed. It advances only after the data is safely written.

**How does it work?** read watermark > pull changes since it > write file > then advance watermark

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- What breaks if the watermark moves first?
- > or >= at the boundary, and why?

## What to do
1. Table + read/advance logic; advance ONLY after the file is written

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look
See the day README's *Where to look in the project* list and the *Read* list.

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.
- watermark DDL + code

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
