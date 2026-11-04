# Day 01: Setup, terminal, git and Python

*Week 1: fundamentals (no AI-written code; AI only as a tutor)*

**Goal:** Get a working dev environment and become comfortable with the terminal, git and Python virtual environments.

> **Project paths.** Where a path is given it is relative to the root of your clone of `saturam-agent-framework`, on the `main` branch. Your own work stays in this folder.

## Read
- Pro Git book, chapters 'Git Basics' and 'Git Branching' (git-scm.com/book)
- docs.python.org tutorial: chapter on virtual environments
- docs.pytest.org: 'Get started'

## Where to look in the project
- `README.md` — project overview and first setup steps
- `scripts/dev_setup.sh` — creates .venv and installs everything; read it BEFORE you run it
- `scripts/test.sh` — how the project runs its tests
- `product/tests/test_landing_contract.py` — the test file you run on day 1
- `CONTRIBUTING.md` — 'Development setup' and 'Pull Request Guidelines'
- `.gitignore` — what the project refuses to commit, and why

## Topics (one folder each)
Open each topic folder's `NOTES.md`. It tells you what to do, where to look in the project, and which files to create in that folder.

| Folder | Topic |
|---|---|
| `terminal/` | Terminal |
| `git/` | Git |
| `python-env/` | Python environments and pytest |
| `project-setup/` | Project setup (saturam-agent-framework) |
| `line-counter/` | Practice: line counter script |

## Hands-on
- [ ] Set up the project and run the unit test file (record test count)
- [ ] Create your learning branch, add LOG.md, commit, push
- [ ] Write the line-counter script and 2 tests by hand
- [ ] Fill NOTES.md + COMMANDS.md in terminal/, git/, python-env/ (see topic folders)

## What the output should look like
Your work is finished when these exist and you can show them:

- [ ] terminal/, git/, python-env/ folders each with NOTES.md and COMMANDS.md filled in
- [ ] project-setup/NOTES.md (steps, errors, test count)
- [ ] line-counter/ script + tests (+ sample.txt)
- [ ] LOG.md and EXPLAIN_BACK.md

## Daily routine
- [ ] Cohort stand-up (15 minutes)
- [ ] Your work is in the topic folders (code, worksheets, `ACTIVITY_LOG.md`)
- [ ] `LOG.md` filled: what I learned, 3 things that surprised me, 1 question I still have
- [ ] Buddy reviewed my code before a mentor saw it (explain to your buddy, never write their code)
- [ ] Small commits, messages say what changed; no keys, `.env` or real data committed
- [ ] Pull request raised from `day-01-<topic>` into `main`

## Demo
Your branch on GitHub with LOG.md and the script; tests passing in your terminal.

## Explain back
A mentor asks these out loud. Prepare your own answers; there is nothing to write down for them.

- [ ] What is a virtual environment and why does this project use one?
- [ ] What is the difference between git merge and git rebase?
- [ ] What does each of your two tests prove? What bug would each catch?

## Done when
Setup works, both tests pass, and you can answer the three questions without notes.

## Notes for this day
- Do not commit __pycache__/ or .venv/. Add a .gitignore on day 1.
- If you cannot access saturam-agent-framework, tell the reviewer immediately; do not wait.
