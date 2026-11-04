# Postgres in Docker (project way)

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 02: Servers, processes, ports and Docker** · [day README](../README.md)

## Understand it first (before you do anything)
Before the steps, answer these in your `ACTIVITY_LOG.md`, in your own words (read the docs first):
- What is this, in one or two sentences of your own?
- How does it work, step by step? Draw the flow.
- Why do we need it? What would go wrong without it?
- How will you know it is working? What would you check?

## What to do
1. Read ./cookbook/scripts/run_pgvector.sh and explain EVERY flag line by line
2. psql -h localhost -p 5532 -U ai: create database, table, insert 2 rows
3. Experiment: stop/start (data?) then rm/run (data?) and explain why

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `cookbook/scripts/run_pgvector.sh` — explain every line; note the -v flag and what it means for data
- `deploy/postgres` — Postgres related deploy files

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
