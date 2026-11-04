# Week 1: fundamentals

**Rule this week:** no AI-written code. AI is a tutor only (explain, don't write). Read the official docs first.

**Outcome:** by Friday you can work comfortably in a terminal, use git properly, run services in Docker, write SQL (including latest-row-per-key on JSON), and call an API safely.

## Days
| Day | Topic |
|---|---|
| [01](./day-01-setup-terminal-git-python/README.md) | Setup, terminal, git, Python |
| [02](./day-02-servers-processes-ports-docker/README.md) | Processes, ports, Docker |
| [03](./day-03-postgresql-basics/README.md) | PostgreSQL basics |
| [04](./day-04-json-and-latest-row-per-key/README.md) | JSON and latest row per key |
| [05](./day-05-http-and-apis/README.md) | HTTP and APIs |

## Additional go-through (basics to be comfortable with)
Not graded as separate days, but you will be asked about them. For each, record it in that day's `LOG.md` under a heading "Additional topics" (what it is, one example you ran, one thing that confused you). Do them alongside the day shown.

| Alongside | Topic | What to understand |
|---|---|---|
| Day 1 | Shell scripts | Read `scripts/dev_setup.sh` line by line: shebang, `set -e`, variables, `if`, functions, exit codes (`echo $?`). |
| Day 1 | File permissions | `ls -l`, `chmod +x`, owner/group/other, why a script says "permission denied". |
| Day 1 | SSH keys for GitHub | `ssh-keygen`, public vs private key, adding the key to GitHub, why the private key is never shared. |
| Day 1 | Git extras | Resolve a merge conflict on purpose; good commit messages; `.gitignore`; what `origin` and `HEAD` are; `git stash`. |
| Day 1 | Python basics | Types, lists/dicts/sets, functions, f-strings, loops/comprehensions, `with open(...)`, exceptions (`try/except`), `import`, `if __name__ == "__main__"`. |
| Day 1 | `json` module and `argparse` | Read/write JSON; accept a filename and a word from the command line. |
| Day 1 | pytest extras | Fixtures, `parametrize`, `tmp_path`, testing that an exception is raised (`pytest.raises`). |
| Day 2 | Docker extras | What a Dockerfile is (read one, don't write yet), environment variables (`-e`), `docker exec`, container networks (overview). |
| Day 2 | Linux basics | `df`, `du`, `top`/`htop`, `curl localhost:PORT`, reading logs. |
| Day 3 | SQL extras | `DISTINCT`, `CASE WHEN`, subqueries, CTEs (`WITH`), `UNION`, `LIKE`/`ILIKE`, date functions, string functions. |
| Day 3 | Design basics | Primary vs foreign key, one-to-many, why we avoid duplicating data, simple ER diagram by hand. |
| Day 3 | Constraints and views | `NOT NULL`, `UNIQUE`, `CHECK`, `CREATE VIEW` (needed in week 3). |
| Day 4 | `ON CONFLICT` (upsert) | `INSERT ... ON CONFLICT DO NOTHING / DO UPDATE` (needed in week 3). |
| Day 4 | `EXPLAIN` | Read a simple plan; see seq scan vs index scan. |
| Day 4 | Time zones | UTC, `timestamptz`, ISO 8601 (`2026-09-01T10:00:00Z`). Why we store UTC. |
| Day 5 | REST idioms | Idempotent vs non-idempotent methods, query parameters vs body, timeouts. |
| Day 5 | `requests`/`httpx` extras | Sessions, timeouts, `raise_for_status`, handling invalid JSON. |
| Day 5 | OAuth and webhooks (overview) | What OAuth tokens/refresh tokens are; what a webhook is; why polling with `since` is used instead. |
| Any | Debugging | Read a traceback bottom-up; `print`/`logging`; `python -m pdb` or breakpoint(); reproduce, then minimise. |
| Any | How to ask for help | Write: goal, what you tried, exact error, what you expect. Max 45 minutes stuck. |
| Any | Security hygiene | No secrets or real data in git/chat; `.env` in `.gitignore`; what to do if you commit a token (tell the reviewer, rotate it). |

## End-of-week check
- Short SQL test on Day 4 data.
- 15-minute explain-back of any two days chosen by the reviewer.
