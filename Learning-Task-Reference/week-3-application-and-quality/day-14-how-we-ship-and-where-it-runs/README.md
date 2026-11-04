# Day 14: How we ship, and where it runs

*Week 3: the EnterpriseGPT application, quality and capstone design*

**Goal:** Follow the team's delivery process and understand how the system is deployed.

> **Project paths.** Every path below is relative to the root of your clone of `saturam-agent-framework`, on the `main` branch (clone: `git clone https://github.com/Saturam-Inc/saturam-agent-framework.git`). If a path is missing, check you are on `main` and tell your buddy or mentor.

## Step 1. Understand first (before touching code)
Be able to explain each of these in your own words before the hands-on part.

- Branch > commit > PR template > format > validate > CI > review
- What validate.sh catches that your tests do not
- Cookbook convention: README.md + TEST_LOG.md (model: cookbook/08_learning/)
- Where it runs: Dockerfile, compose, Azure (overview), secrets in Key Vault

## Read
- .github/pull_request_template.md
- cookbook/08_learning/
- deploy/Dockerfile, deploy/compose.yaml
- deploy/AZURE_CUTOVER.md (overview only)

## Where to look in the project
- `.github/pull_request_template.md` — the PR template you must fill
- `.github/workflows/ci.yml` — what CI runs on your PR
- `.github/workflows/pr-lint.yml` — PR title/format rules
- `scripts/format.sh` — formats code
- `scripts/validate.sh` — lints and type-checks
- `CONTRIBUTING.md` — 'Pull Request Guidelines', 'Formatting and validation', 'Local testing'
- `CODEOWNERS` — who reviews what
- `cookbook/STYLE_GUIDE.md` — how cookbooks are written
- `cookbook/08_learning/README.md` — the model cookbook: README + TEST_LOG shape
- `cookbook/08_learning/TEST_LOG.md` — what a TEST_LOG looks like
- `deploy/Dockerfile` — how the image is built
- `deploy/compose.yaml` — how services run together
- `deploy/AZURE_CUTOVER.md` — Azure overview (read overview only)

## Topics (one folder each)
Open each topic folder's `NOTES.md`. It tells you what to do, where to look in the project, and which files to create in that folder.

| Folder | Topic |
|---|---|
| `practice-pr/` | Practice PR |
| `cookbook-style/` | Cookbook style |
| `deploy-overview/` | Deploy overview |
| `buddy-review/` | Reviewing a buddy's PR |

## Hands-on lab
**Time:** about 3 hours · **You will build:** a reviewed practice PR and a README + TEST_LOG in the team's cookbook style

1. In a scratch branch of your `saturam-agent-framework` clone (never push), run `./scripts/format.sh` and `./scripts/validate.sh`; record what they check.
2. Read `cookbook/08_learning/README.md` and `TEST_LOG.md`. Write the same two files for your day-10 workflow.
3. Open a practice PR in your learning repo using the PR template text; make format and validate pass.
4. Review your buddy's PR with a checklist; write three useful comments.
5. Read `deploy/Dockerfile` line by line and draw where the app, Postgres and secrets live.

**Expected output:** Passing format/validate output, a PR link, three review comments, a README + TEST_LOG, and a deploy diagram.

**Break it on purpose:** Introduce a deliberate lint or type error and watch validate catch it. What did your tests not catch?

**Reflect (write the answer in the topic's `ACTIVITY_LOG.md`):** What does a human reviewer catch that the tools cannot?

### Checklist
- [ ] Format + validate pass
- [ ] Open practice PR and get a review
- [ ] Write README + TEST_LOG
- [ ] Review your buddy's PR

## What the output should look like
Your work is finished when these exist and you can show them:

- [ ] PR link with passing checks
- [ ] buddy-review/REVIEW_NOTES.md with your 3 comments
- [ ] cookbook-style/README.md and TEST_LOG.md following the model
- [ ] deploy-overview/DIAGRAM

## Think it through yourself
No answer is given here. Decide, try, and write your reasoning in the topic's `ACTIVITY_LOG.md`.

- What kinds of mistakes does a human reviewer catch that tools cannot?
- Why does a secret in Git history stay a problem even after deletion?

## Suggested tools
- ruff / the repo's format.sh and validate.sh
- pre-commit (optional)
- gh CLI for PRs
- hadolint (optional) to lint Dockerfiles

## Daily routine
- [ ] Cohort stand-up (15 minutes)
- [ ] Your work is in the topic folders (code, worksheets, `ACTIVITY_LOG.md`)
- [ ] `LOG.md` filled: what I learned, 3 things that surprised me, 1 question I still have
- [ ] Buddy reviewed my code before a mentor saw it (explain to your buddy, never write their code)
- [ ] Small commits, messages say what changed; no keys, `.env` or real data committed
- [ ] Pull request raised from `day-14-<topic>` into `main`

## Demo
Show your PR passing, your review comments on your buddy's PR, and the deploy diagram.

## Explain back
A mentor asks these out loud. Prepare your own answers; there is nothing to write down for them.

- [ ] What does validate.sh catch that your tests do not?
- [ ] Walk through the Dockerfile.
- [ ] Where does a model key live in production and why?

## Done when
Your PR passes format and validate and you can explain each deploy file.

## Notes for this day
- End of week 3 check: 20-minute explain-back on days 11-14 plus a short quiz on semantic layer, evals and shipping.
