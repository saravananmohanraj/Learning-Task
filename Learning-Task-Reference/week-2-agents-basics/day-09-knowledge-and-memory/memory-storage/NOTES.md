# Memory and storage

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 09: Knowledge and memory** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** Storage keeps the conversation (session history). Memory keeps facts learned about a user or context across sessions. Knowledge holds documents you provide.

**How does it work?** run > messages saved to db by session_id > next run loads history > memory manager extracts lasting facts > recalled in later sessions

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- What survives a restart, and what does not?
- What is the difference between session history and memory?
- What are the privacy risks of memory?

## What to do
1. Add storage so a conversation survives a restart
2. Show a second session remembering the first; show what it does NOT remember

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `cookbook/00_quickstart/agent_with_storage.py`
- `cookbook/00_quickstart/agent_with_memory.py`
- `cookbook/11_memory/01_agent_with_memory.py`

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
