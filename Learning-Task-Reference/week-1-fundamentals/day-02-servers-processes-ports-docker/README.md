# Day 02: Servers, processes, ports and Docker

*Week 1: fundamentals (no AI-written code; AI only as a tutor)*

**Goal:** Understand what a running service is, and be able to start, inspect, connect to and stop Postgres in Docker.

> **Project paths.** Where a path is given it is relative to the root of your clone of `saturam-agent-framework`, on the `main` branch. Your own work stays in this folder.

## Read
- docs.docker.com 'Get started', parts 1 to 3
- man pages: ps, lsof, kill

## Where to look in the project
- `cookbook/scripts/run_pgvector.sh` — how the project starts Postgres (every flag is on your explain list)
- `deploy/compose.yaml` — the real multi-container set-up; list its services, images, ports
- `deploy/Dockerfile` — how the application image is built (read only)
- `deploy/README.md` — how deploy files fit together

## Topics (one folder each)
Open each topic folder's `NOTES.md`. It tells you what to do, where to look in the project, and which files to create in that folder.

| Folder | Topic |
|---|---|
| `processes-ports/` | Processes and ports |
| `docker/` | Docker |
| `compose/` | docker compose |
| `postgres-container/` | Postgres in Docker (project way) |

## Hands-on
- [ ] Run Postgres with run_pgvector.sh; find container, logs and port
- [ ] Connect with psql; create a db, table, 2 rows
- [ ] Stop/start, then remove/recreate; record results
- [ ] Table of services/images/ports from deploy/compose.yaml

## What the output should look like
Your work is finished when these exist and you can show them:

- [ ] processes-ports/, docker/, compose/ with NOTES.md + COMMANDS.md
- [ ] postgres-container/FLAGS.md (every flag explained) and EXPERIMENT.md (stop vs rm results)
- [ ] compose/SERVICES.md (table)
- [ ] LOG.md and EXPLAIN_BACK.md

## Daily routine
- [ ] Cohort stand-up (15 minutes)
- [ ] Your work is in the topic folders (code, worksheets, `ACTIVITY_LOG.md`)
- [ ] `LOG.md` filled: what I learned, 3 things that surprised me, 1 question I still have
- [ ] Buddy reviewed my code before a mentor saw it (explain to your buddy, never write their code)
- [ ] Small commits, messages say what changed; no keys, `.env` or real data committed
- [ ] Pull request raised from `day-02-<topic>` into `main`

## Demo
Show the running container, connect with psql, show your table, explain data on stop vs remove.

## Explain back
A mentor asks these out loud. Prepare your own answers; there is nothing to write down for them.

- [ ] What does -p 5532:5432 mean? Which number is on your laptop and which inside the container?
- [ ] Why did data survive a stop but not a remove (or did it)? What is a volume?
- [ ] Two services in compose.yaml want the same port. What happens?

## Done when
You can start, inspect, connect to and stop Postgres without looking anything up.

## Notes for this day
- Read run_pgvector.sh carefully, especially the `-v` flag. Before you test stop/start and remove/recreate, write down what you predict will happen to your table in each case, then compare with what you saw.
