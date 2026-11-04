# Reading a run trace and tracing the code

> Guide for this topic. Do the work, then keep **everything you produce in this folder**: code, SQL, worksheets, screenshots, and your activity log.

**Day 07: Your first agent** · [day README](../README.md)

## Understand it first (before you do anything)
**What is it?** Debug output shows the real messages, the model's reply and the token counts of a run. It is how you learn what an agent actually did.

**How does it work?** Agent.run > run_dispatch/_run (agent/_run.py) > get_run_messages (agent/_messages.py) > model call (models/base.py) > tool handling > response conversion (agent/_response.py)

**Answer these in your `ACTIVITY_LOG.md` before you start the steps:**
- What was in the system message? Where did it come from?
- Which messages were added by the framework and not by you?
- How many tokens went in and out, and what does that cost?

## What to do
1. Turn on debug output (debug_mode) and read one full run: messages sent, model reply, tokens used; annotate it by hand
2. Match every part of the trace to your day-6 loop (messages, model call, parse)
3. Trace the code: Agent run > run_dispatch and _run in libs/agno/egpt/agent/_run.py > get_run_messages in _messages.py > the model call in libs/agno/egpt/models/base.py; write file, function and one line on what each does

Work through these in order. After each step, write down what you expected, what really happened, and why.

## Where to look in the project
- `libs/agno/egpt/agent/_run.py` — _run and run_dispatch
- `libs/agno/egpt/agent/_messages.py` — get_system_message, get_run_messages
- `libs/agno/egpt/models/base.py` — response() loop

## Put your work in this folder
- `ACTIVITY_LOG.md` — your worksheet. For each activity: date, what you did, the exact commands / queries / prompts you ran, what you saw (paste real output, never keys), what went wrong and how you fixed it, and what you could now explain to someone else.
- annotated trace
- code path (file + function + one line each)

## This topic is done when
- Every step above has an entry in `ACTIVITY_LOG.md` with output you saw yourself
- Everything you built is in this folder and runs
- You can explain each step and each line of your code without notes
