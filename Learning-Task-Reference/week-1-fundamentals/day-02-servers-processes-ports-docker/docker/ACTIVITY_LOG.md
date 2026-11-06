About Docker:
-> It is a platform that packages applications and their dependencies into isolated, standardized units called containers.
-> Ensuring the software runs consistently on any machine.

Flow:
1. A Dockerfile provides instructions to build a static blueprint called an Image. 
2. Docker then runs this Image as a Container.
3. It shares the host OS kernel but operates in an isolated environment with its own filesystem, network, and processes.

Why Docker?
-> It eliminates the "it works on my machine" problem. 
-> Without it, you risk conflicting software versions, missing dependencies, and application environments that are difficult to reproduce across different developer laptops and production servers.

How will i know it's working?
-> You can run docker ps to verify the container's status is "Up"
-> Check docker logs <container_name> for successful startup messages, and successfully connect a client to its mapped port.

Execution log:

About Images vs Containers analogy:
Images -> Blue print
Containers -> using blueprint, we can build it.
Eg: Building the house using the blue prints.

Using single blueprint, we can also create multiple containers.
Something affects in containers, the original blueprint is perfect.

Execution log:

1. docker run command
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker run -d --name my-db -e POSTGRES_PASSWORD=secret -p 5532:5432 postgres
4687c897d8749e53746c58de59de727aae31c2ad8e3b7ceb464ff0fcf2542310

-> Downloads the Postgres image if missing, starts a container in the background (-d), names it my-db, sets a password environment variable (-e), and maps ports (-p).

2. docker ps command
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker ps
CONTAINER ID   IMAGE      COMMAND                  CREATED         STATUS         PORTS                                         NAMES
4687c897d874   postgres   "docker-entrypoint.s…"   3 seconds ago   Up 3 seconds   0.0.0.0:5532->5432/tcp, [::]:5532->5432/tcp   my-db

-> Lists currently running containers.

3. docker ps -a command
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker ps -a
CONTAINER ID   IMAGE                                 COMMAND                  CREATED         STATUS                       PORTS                                                                                                                                  NAMES
4687c897d874   postgres                              "docker-entrypoint.s…"   7 seconds ago   Up 6 seconds                 0.0.0.0:5532->5432/tcp, [::]:5532->5432/tcp                                                                                            my-db
85aa5c1e03fe   postgres:alpine                       "docker-entrypoint.s…"   9 days ago      Exited (1) 9 days ago                                                                                                                                               admiring_volhard
f879d5a35ca0   agnohq/pgvector:18                    "docker-entrypoint.s…"   2 weeks ago     Exited (255) 9 minutes ago   0.0.0.0:5532->5432/tcp                                                                                                                 egpt-retail-postgres-1
b6f856b48ee8   gcr.io/k8s-minikube/kicbase:v0.0.50   "/usr/local/bin/entr…"   5 months ago    Exited (255) 2 weeks ago     127.0.0.1:32768->22/tcp, 127.0.0.1:32769->2376/tcp, 127.0.0.1:32770->5000/tcp, 127.0.0.1:32771->8443/tcp, 127.0.0.1:32772->32443/tcp   minikube
4fe439d4d130   sonarqube:latest                      "/opt/sonarqube/dock…"   14 months ago   Exited (130) 14 months ago                                                                                                                                          festive_wu
4724e99f37c0   sonarqube:lts-community               "/opt/sonarqube/dock…"   14 months ago   Exited (130) 14 months ago                                                                                                                                          sleepy_lovelace
9f9c12a76872   sonarqube:latest                      "/opt/sonarqube/dock…"   14 months ago   Exited (130) 14 months ago                                                                                                                                          wizardly_curran
1fb468a84605   sonarqube                             "/opt/sonarqube/dock…"   14 months ago   Exited (255) 14 months ago                                                                                                                                          sonarqube
3481d1749d0f   postgres:alpine                       "docker-entrypoint.s…"   14 months ago   Exited (255) 14 months ago   5432/tcp                                                                                                                               sonarqube-db
36ef4d640af8   sonarqube:lts-community               "/opt/sonarqube/dock…"   14 months ago   Exited (255) 14 months ago   9000/tcp                                                                                                                               flamboyant_edison
5fe3498b945e   sonarqube:lts-community               "/opt/sonarqube/dock…"   14 months ago   Exited (255) 14 months ago   0.0.0.0:9000->9000/tcp                                                                                                                 sonar
7ee8c04d30bf   flask-docker                          "python3 -m flask ru…"   14 months ago   Exited (0) 14 months ago                                                                                                                                            strange_booth

-> Lists currently running containers, with stopped ones.

4. docker logs command
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker logs -f my-db
The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

The database cluster will be initialized with locale "en_US.utf8".
The default database encoding has accordingly been set to "UTF8".
The default text search configuration will be set to "english".

Data page checksums are enabled.

fixing permissions on existing directory /var/lib/postgresql/18/docker ... ok
creating subdirectories ... ok
selecting dynamic shared memory implementation ... posix
selecting default "max_connections" ... 100
selecting default "shared_buffers" ... 128MB
selecting default time zone ... Etc/UTC
creating configuration files ... ok
running bootstrap script ... ok
performing post-bootstrap initialization ... ok
syncing data to disk ... ok


Success. You can now start the database server using:

    pg_ctl -D /var/lib/postgresql/18/docker -l logfile start

initdb: warning: enabling "trust" authentication for local connections
initdb: hint: You can change this by editing pg_hba.conf or using the option -A, or --auth-local and --auth-host, the next time you run initdb.
waiting for server to start....2026-11-05 05:59:16.005 UTC [53] LOG:  starting PostgreSQL 18.6 (Debian 18.6-1.pgdg13+2) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
2026-11-05 05:59:16.007 UTC [53] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-11-05 05:59:16.018 UTC [59] LOG:  database system was shut down at 2026-11-05 05:59:15 UTC
2026-11-05 05:59:16.023 UTC [53] LOG:  database system is ready to accept connections
 done
server started

/usr/local/bin/docker-entrypoint.sh: ignoring /docker-entrypoint-initdb.d/*

waiting for server to shut down....2026-11-05 05:59:16.174 UTC [53] LOG:  received fast shutdown request
2026-11-05 05:59:16.177 UTC [53] LOG:  aborting any active transactions
2026-11-05 05:59:16.179 UTC [53] LOG:  background worker "logical replication launcher" (PID 62) exited with exit code 1
2026-11-05 05:59:16.179 UTC [57] LOG:  shutting down
2026-11-05 05:59:16.182 UTC [57] LOG:  checkpoint starting: shutdown immediate
2026-11-05 05:59:16.192 UTC [57] LOG:  checkpoint complete: wrote 0 buffers (0.0%), wrote 3 SLRU buffers; 0 WAL file(s) added, 0 removed, 0 recycled; write=0.003 s, sync=0.002 s, total=0.014 s; sync files=2, longest=0.001 s, average=0.001 s; distance=0 kB, estimate=0 kB; lsn=0/1761918, redo lsn=0/1761918
2026-11-05 05:59:16.202 UTC [53] LOG:  database system is shut down
 done
server stopped

PostgreSQL init process complete; ready for start up.

2026-11-05 05:59:16.303 UTC [1] LOG:  starting PostgreSQL 18.6 (Debian 18.6-1.pgdg13+2) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
2026-11-05 05:59:16.304 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2026-11-05 05:59:16.304 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2026-11-05 05:59:16.309 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2026-11-05 05:59:16.318 UTC [73] LOG:  database system was shut down at 2026-11-05 05:59:16 UTC
2026-11-05 05:59:16.323 UTC [1] LOG:  database system is ready to accept connections

-> Streams the live output logs. Press Ctrl+C to exit the stream.

5. docker inspect command
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker inspect my-db
[
    {
        "Id": "4687c897d8749e53746c58de59de727aae31c2ad8e3b7ceb464ff0fcf2542310",
        "Created": "2026-11-05T05:59:14.654134637Z",
        "Path": "docker-entrypoint.sh",
        "Args": [
            "postgres"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 1079,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2026-11-05T05:59:14.783624258Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:3a4264520e121176619f54ff867d12774bc81e95e7b84db58d63bccdb6144b81",
        "ResolvConfPath": "/var/lib/docker/containers/4687c897d8749e53746c58de59de727aae31c2ad8e3b7ceb464ff0fcf2542310/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/4687c897d8749e53746c58de59de727aae31c2ad8e3b7ceb464ff0fcf2542310/hostname",
        "HostsPath": "/var/lib/docker/containers/4687c897d8749e53746c58de59de727aae31c2ad8e3b7ceb464ff0fcf2542310/hosts",
        "LogPath": "/var/lib/docker/containers/4687c897d8749e53746c58de59de727aae31c2ad8e3b7ceb464ff0fcf2542310/4687c897d8749e53746c58de59de727aae31c2ad8e3b7ceb464ff0fcf2542310-json.log",
        "Name": "/my-db",
        "RestartCount": 0,
        "Driver": "overlayfs",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "bridge",
            "PortBindings": {
                "5432/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "5532"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "ConsoleSize": [
                48,
                172
            ],
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": [],
            "BlkioDeviceWriteBps": [],
            "BlkioDeviceReadIOps": [],
            "BlkioDeviceWriteIOps": [],
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": [],
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/interrupts",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware",
                "/sys/devices/virtual/powercap"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": null,
            "Name": "overlayfs"
        },
        "Mounts": [
            {
                "Type": "volume",
                "Name": "f617f732dceb0e3eeb471f6fa8417c2a42c848ca071f173d8f15b6dc11ffe308",
                "Source": "/var/lib/docker/volumes/f617f732dceb0e3eeb471f6fa8417c2a42c848ca071f173d8f15b6dc11ffe308/_data",
                "Destination": "/var/lib/postgresql",
                "Driver": "local",
                "Mode": "",
                "RW": true,
                "Propagation": ""
            }
        ],
        "Config": {
            "Hostname": "4687c897d874",
            "Domainname": "",
            "User": "",
            "AttachStdin": false,
            "AttachStdout": false,
            "AttachStderr": false,
            "ExposedPorts": {
                "5432/tcp": {}
            },
            "Tty": false,
            "OpenStdin": false,
            "StdinOnce": false,
            "Env": [
                "POSTGRES_PASSWORD=secret",
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/lib/postgresql/18/bin",
                "GOSU_VERSION=1.19",
                "LANG=en_US.utf8",
                "PG_MAJOR=18",
                "PG_VERSION=18.6-1.pgdg13+2",
                "PGDATA=/var/lib/postgresql/18/docker"
            ],
            "Cmd": [
                "postgres"
            ],
            "Image": "postgres",
            "Volumes": {
                "/var/lib/postgresql": {}
            },
            "WorkingDir": "",
            "Entrypoint": [
                "docker-entrypoint.sh"
            ],
            "OnBuild": null,
            "Labels": {},
            "StopSignal": "SIGINT"
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "49985aade346498c373150e50bcfe1c3e239c3037d9a87089ffc6051aeb4b545",
            "SandboxKey": "/var/run/docker/netns/49985aade346",
            "Ports": {
                "5432/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "5532"
                    },
                    {
                        "HostIp": "::",
                        "HostPort": "5532"
                    }
                ]
            },
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "ac934da0a5322a62ab5394dd1db167e59a08a6e147da4c178caf0a5b6c5723c6",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "66:af:b9:06:eb:a2",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "MacAddress": "66:af:b9:06:eb:a2",
                    "DriverOpts": null,
                    "GwPriority": 0,
                    "NetworkID": "8b2c6e0bcd479dc5745fc0b1468ed55c3dd7c8769a4f5fe0ff4d2b58758dcacb",
                    "EndpointID": "ac934da0a5322a62ab5394dd1db167e59a08a6e147da4c178caf0a5b6c5723c6",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "DNSNames": null
                }
            }
        },
        "ImageManifestDescriptor": {
            "mediaType": "application/vnd.oci.image.manifest.v1+json",
            "digest": "sha256:f4b419e350fd98d4a8429603295208976dea4c8fb8326d818d346d3e29f1db6f",
            "size": 3439,
            "annotations": {
                "com.docker.official-images.bashbrew.arch": "amd64",
                "org.opencontainers.image.base.digest": "sha256:1e1a22175fbf1b32157ddaf0219e1db4e5401fab2b94ed285add64d18587cd2d",
                "org.opencontainers.image.base.name": "debian:trixie-slim",
                "org.opencontainers.image.created": "2026-10-28T01:30:07Z",
                "org.opencontainers.image.revision": "e00e1bd34ec5c8a8e7ad89b273b3d42efaf6d5bc",
                "org.opencontainers.image.source": "https://github.com/docker-library/postgres.git#e00e1bd34ec5c8a8e7ad89b273b3d42efaf6d5bc:18/trixie",
                "org.opencontainers.image.url": "https://hub.docker.com/_/postgres",
                "org.opencontainers.image.version": "18.6"
            },
            "platform": {
                "architecture": "amd64",
                "os": "linux"
            }
        }
    }
]

-> Outputs low-level JSON configuration details about the container's network and volumes.

6. docker images command
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker images
REPOSITORY                    TAG             IMAGE ID       CREATED         SIZE
postgres                      latest          3a4264520e12   8 days ago      644MB
egpt-retail                   dev             8d1cf7aead26   2 weeks ago     789MB
localstack/localstack-pro     latest          503a65fbf60e   5 months ago    1.82GB
gcr.io/k8s-minikube/kicbase   <none>          eb4fec00e8ad   8 months ago    1.94GB
agnohq/pgvector               18              e502d095cfb0   11 months ago   737MB
postgres                      alpine          3406990b6e4c   14 months ago   398MB
flask-docker                  latest          928d514ee6bb   14 months ago   196MB
sonarqube                     latest          6d64b6cdec73   15 months ago   2.18GB
sonarqube                     lts-community   f98a29395d77   15 months ago   1.02GB

-> Lists all the downloaded images currently stored on your machine

7. docker stop command
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker stop my-db
my-db

-> Gracefully halts the container process.

8. docker start command
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker start my-db
my-db

-> Resumes the halted container.

9. docker rm command
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker stop my-db
my-db
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker rm my-db
my-db

-> Deletes the container completely. It must be stopped first.

10. docker exec command
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker exec -it my-db bash
root@92246ef179b6:/# ls
bin  boot  dev  docker-entrypoint-initdb.d  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@92246ef179b6:/#

-> Opens an interactive terminal session inside the running container.


Port Mapping HOST:CONTAINER

When you use the -p flag 5532:5432

5532 -> Port opened in our windows desktop
5432 -> Internal port the Postgres service is listening on inside the isolated Docker environment.

Any traffic sent to localhost:5532 on our local machine gets automatically forwarded through the Docker network boundary into port 5432 of the container.


Volume: Proving what survives

1. No volume (Ephemeral)

(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker exec -it my-db bash
root@92246ef179b6:/# psql -U postgres
psql (18.6 (Debian 18.6-1.pgdg13+2))
Type "help" for help.

postgres=# CREATE TABLE dummy (id SERIAL, note TEXT);
CREATE TABLE
postgres=# INSERT INTO dummy (note) VALUES ('Testing Docker persistence');
INSERT 0 1
postgres=# SELECT * FROM dummy;
 id |            note
----+----------------------------
  1 | Testing Docker persistence
(1 row)

postgres=# \q
root@92246ef179b6:/# exit
exit
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker stop my-db
my-db
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker rm my-db
my-db
(.venv)

-> Again running the docker run command, data has been lost.
-> Without volume, all data is tied to the lifecycle of that specific container instance and is destroyed upon removal.

2. Named Volume (docker-managed)

SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker run -d --name test-db -e POSTGRES_PASSWORD=secret -v my_pg_data:/var/lib/postgresql/data postgres:16
Unable to find image 'postgres:16' locally
16: Pulling from library/postgres
28d8a96df569: Pull complete
dc3e98153fd4: Pull complete
7ee6ed8de1c8: Pull complete
c60d02d02e9b: Pull complete
b355a8fcc1d3: Pull complete
5c4d204f6daa: Pull complete
Digest: sha256:5db6dac2ef5dcff512f4f00a009c3c332b9f2f28f24277175bf3e4a3d02ef83a
Status: Downloaded newer image for postgres:16
33d110f08cb3b4f5dff34df63a5b71eb574b16e26a56007e52f7205a12db38a0
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker exec -it test-db bash
root@33d110f08cb3:/# psql -U postgres
psql (16.15 (Debian 16.15-1.pgdg13+2))
Type "help" for help.

postgres=# create table test (notes int);
CREATE TABLE
postgres=# insert table test (notes) values(1);
ERROR:  syntax error at or near "table"
LINE 1: insert table test (notes) values(1);
               ^
postgres=# insert into table test (notes) values(1);
ERROR:  syntax error at or near "table"
LINE 1: insert into table test (notes) values(1);
                    ^
postgres=# insert into test (notes) values(1);
INSERT 0 1
postgres=# \q
root@33d110f08cb3:/# exit
exit
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker stop test-db
test-db
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker rm test-db
test-db


SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker run -d --name test-db-2 -e POSTGRES_PASSWORD=secret -v my_pg_data:/var/lib/postgresql/data postgres:16
724ced76291c260c7e3c62dda6b5379c7a39645bdc5234eb1ae4b1c651d304a0
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker exec -it test-db-2 bash
root@724ced76291c:/# psql -U postgres
psql (16.15 (Debian 16.15-1.pgdg13+2))
Type "help" for help.

postgres=# select * from test;
 notes
-------
     1
(1 row)

-> The table survives. The -v my_pg_data:... flag tells Docker to safely store the database files in a managed volume on your hard drive, which persists independently of the container.

3. Bind Mount (Host-managed)

SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker run -d --name test-bind -e POSTGRES_PASSWORD=secret -v $(pwd)/pg_local:/var/lib/postgresql/data postgres:16
e1dba104b1045046d3f6eeda95253a3f029492cfcc7e878931c29ce5d9c41d76
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker exec -it test-bind bash
root@e1dba104b104:/# psql -u postgres
/usr/lib/postgresql/16/bin/psql: invalid option -- 'u'
psql: hint: Try "psql --help" for more information.
root@e1dba104b104:/# psql -U postgres
psql (16.15 (Debian 16.15-1.pgdg13+2))
Type "help" for help.

postgres=# create table test (notes int);
CREATE TABLE
postgres=# insert into test (notes) values (1);
INSERT 0 1
postgres=# \q
root@e1dba104b104:/# exit
exit
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker stop test-bind
test-bind
(.venv)
SMS@DESKTOP-G2PRDKV MINGW64 /c/Saturam/saturam-agent-framework (main)
$ docker rm test-bind
test-bind
(.venv)


-> The table survives, and you will physically see a new pg_local folder appear directly in your VS Code workspace. 
-> A bind mount maps a specific, visible directory from your Windows host directly into the container.