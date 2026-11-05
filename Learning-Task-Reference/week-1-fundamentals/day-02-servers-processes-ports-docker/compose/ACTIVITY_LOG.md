About Compose:
-> It is a tool that allows you to define and manage multi-containers docker applications using a single YAML configiration file.

Flow:
1. Write a compose.yaml file defining your services, networks, and volumes.
2. Run docker compose up
3. The Compose engine reads the file, sets up the shared network, creates the volumes
4. It starts all the containers in the correct dependency order.

Why Compose?
-> Without it, running an application that requires multiple containers means typing out multiple long docker run commands with complex network and volume flags every time. 
-> Compose turns all that operational complexity into a single, version-controllable file.

How will i know it's working?
-> Run docker compose ps in the directory containing the YAML file to see all grouped containers running together.
-> Docker compose logs to see a unified stream of output from all interconnected services.

Execution logs:

1. docker compose up command
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 ~/Downloads/Learning-Task-Reference/Learning-Task-Reference/week-1-fundamentals/day-02-servers-processes-ports-docker/compose (day-02-servers-processes-ports-docker)
$ docker compose up -d
[+] Running 2/2
 ✔ Network compose_default         Created                                                                                                                             0.1s
 ✔ Container compose-my-test-db-1  Started                                                                                                                             0.4s

-> Starts the services defined in the YAML file in the background.

 2. docker compose ps command
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 ~/Downloads/Learning-Task-Reference/Learning-Task-Reference/week-1-fundamentals/day-02-servers-processes-ports-docker/compose (day-02-servers-processes-ports-docker)
$ docker compose ps
NAME                   IMAGE         COMMAND                  SERVICE      CREATED          STATUS          PORTS
compose-my-test-db-1   postgres:16   "docker-entrypoint.s…"   my-test-db   11 seconds ago   Up 10 seconds   0.0.0.0:5533->5432/tcp, [::]:5533->5432/tcp

-> Lists the running containers managed by this specific compose file.

3. docker compose logs
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 ~/Downloads/Learning-Task-Reference/Learning-Task-Reference/week-1-fundamentals/day-02-servers-processes-ports-docker/compose (day-02-servers-processes-ports-docker)
$ docker compose logs
my-test-db-1  | The files belonging to this database system will be owned by user "postgres".
my-test-db-1  | This user must also own the server process.
my-test-db-1  |
my-test-db-1  | The database cluster will be initialized with locale "en_US.utf8".
my-test-db-1  | The default database encoding has accordingly been set to "UTF8".
my-test-db-1  | The default text search configuration will be set to "english".
my-test-db-1  |
my-test-db-1  | Data page checksums are disabled.
my-test-db-1  |
my-test-db-1  | fixing permissions on existing directory /var/lib/postgresql/data ... ok
my-test-db-1  | creating subdirectories ... ok
my-test-db-1  | selecting dynamic shared memory implementation ... posix
my-test-db-1  | selecting default max_connections ... 100
my-test-db-1  | selecting default shared_buffers ... 128MB
my-test-db-1  | selecting default time zone ... Etc/UTC
my-test-db-1  | creating configuration files ... ok
my-test-db-1  | running bootstrap script ... ok
my-test-db-1  | performing post-bootstrap initialization ... ok
my-test-db-1  | syncing data to disk ... ok
my-test-db-1  | initdb: warning: enabling "trust" authentication for local connections
my-test-db-1  | initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.
my-test-db-1  |
my-test-db-1  |
my-test-db-1  | Success. You can now start the database server using:
my-test-db-1  |
my-test-db-1  |     pg_ctl -D /var/lib/postgresql/data -l logfile start
my-test-db-1  |
my-test-db-1  | waiting for server to start....2026-11-05 07:26:56.238 UTC [49] LOG:  starting PostgreSQL 16.15 (Debian 16.15-1.pgdg13+2) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
my-test-db-1  | 2026-11-05 07:26:56.240 UTC [49] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
my-test-db-1  | 2026-11-05 07:26:56.246 UTC [52] LOG:  database system was shut down at 2026-11-05 07:26:55 UTC
my-test-db-1  | 2026-11-05 07:26:56.253 UTC [49] LOG:  database system is ready to accept connections
my-test-db-1  |  done
my-test-db-1  | server started
my-test-db-1  |
my-test-db-1  | /usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*
my-test-db-1  |
my-test-db-1  | waiting for server to shut down...2026-11-05 07:26:56.383 UTC [49] LOG:  received fast shutdown request
my-test-db-1  | .2026-11-05 07:26:56.386 UTC [49] LOG:  aborting any active transactions
my-test-db-1  | 2026-11-05 07:26:56.388 UTC [49] LOG:  background worker "logical replication launcher" (PID 55) exited with exit code 1
my-test-db-1  | 2026-11-05 07:26:56.388 UTC [50] LOG:  shutting down
my-test-db-1  | 2026-11-05 07:26:56.390 UTC [50] LOG:  checkpoint starting: shutdown immediate
my-test-db-1  | 2026-11-05 07:26:56.402 UTC [50] LOG:  checkpoint complete: wrote 3 buffers (0.0%); 0 WAL file(s) added, 0 removed, 0 recycled; write=0.003 s, sync=0.002 s, total=0.015 s; sync files=2, longest=0.001 s, average=0.001 s; distance=0 kB, estimate=0 kB; lsn=0/14F2AE8, redo lsn=0/14F2AE8
my-test-db-1  | 2026-11-05 07:26:56.405 UTC [49] LOG:  database system is shut down
my-test-db-1  |  done
my-test-db-1  | server stopped
my-test-db-1  |
my-test-db-1  | PostgreSQL init process complete; ready for start up.
my-test-db-1  |
my-test-db-1  | 2026-11-05 07:26:56.506 UTC [1] LOG:  starting PostgreSQL 16.15 (Debian 16.15-1.pgdg13+2) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
my-test-db-1  | 2026-11-05 07:26:56.507 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
my-test-db-1  | 2026-11-05 07:26:56.507 UTC [1] LOG:  listening on IPv6 address "::", port 5432
my-test-db-1  | 2026-11-05 07:26:56.511 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
my-test-db-1  | 2026-11-05 07:26:56.518 UTC [63] LOG:  database system was shut down at 2026-11-05 07:26:56 UTC
my-test-db-1  | 2026-11-05 07:26:56.524 UTC [1] LOG:  database system is ready to accept connections

-> Shows the startup logs for the database

4. docker compose down
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 ~/Downloads/Learning-Task-Reference/Learning-Task-Reference/week-1-fundamentals/day-02-servers-processes-ports-docker/compose (day-02-servers-processes-ports-docker)
$ docker compose down
[+] Running 2/2
 ✔ Container compose-my-test-db-1  Removed                                                                                                                             0.3s
 ✔ Network compose_default         Removed

 -> Stops and removes the containers and the default network it created, but keeps volumes.

 5. docker compose down -v

 -> Stops the containers and also destroys any named volumes attached to them, completely wiping the data.

Test port conflicts:
-> Windows machine only has one Port 5534 available. 
-> Once db-one claims it, db-two crashes because the host port is already occupied, even though the internal container ports are isolated.

(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 ~/Downloads/Learning-Task-Reference/Learning-Task-Reference/week-1-fundamentals/day-02-servers-processes-ports-docker/compose (day-02-servers-processes-ports-docker)
$ docker compose up -d
[+] Running 2/3
 ✔ Network compose_default               Created                                                                                                                       0.1s
 ✔ Container compose-my-test-db-check-1  Started                                                                                                                       0.5s
 - Container compose-my-test-db-1        Starting                                                                                                                      0.5s
Error response from daemon: failed to set up container networking: driver failed programming external connectivity on endpoint compose-my-test-db-1 (6c46c2d2864cb8b7858bbc0d40fd3d66f13826b974e95b1df2fc3d3408296ebb): Bind for 0.0.0.0:5533 failed: port is already allocated


List of services, images and ports on deploy/compose.yaml

| Service Name | Image | Host Port | Container Port |
|---|---|---|---|
| `postgres` | `agnohq/pgvector:18` | `5532` | `5432` |
| `migrate` | `egpt-retail:dev` | *(None mapped)* | *(None mapped)* |
| `warehouse-migrate` | `egpt-retail:dev` | *(None mapped)* | *(None mapped)* |
| `api` | `egpt-retail:dev` | `7777` (or `EGPT_RETAIL_API_PORT`) | `7777` |
| `consolidator` | `egpt-retail:dev` | *(None mapped)* | *(None mapped)* |
| `neo4j` | `neo4j:5` | `7474`, `7687` | `7474`, `7687` |
| `redis` | `redis:7-alpine` | `6379` | `6379` |
| `minio` | `minio/minio:RELEASE.2025-09-07T16-13-09Z` | `9000`, `9001` | `9000`, `9001` |