About postgres-container
-> This is a method of running a PostgreSQL database—specifically one pre-configured with the pgvector extension for storing and querying AI vector embeddings—inside an isolated Docker container rather than installing it directly on the host operating system.

Flow
1. Docker pulls the pre-built agnohq/pgvector:18 image from a container registry.
2. The docker run command instructs the Docker Engine to create an isolated environment (a container) from that image.
3. Environment variables (-e) pass startup configuration (database name, user, password) to the Postgres initialization process.
4. A named volume (-v) is attached to the container to store the actual database files on the host's filesystem, bypassing the container's ephemeral layer.
5. A port map (-p) bridges the host network (port 5532) to the container's internal network (port 5432), allowing external tools to connect.

Why postgres container?
-> It provides immediate, reproducible, and standardized database environments across different machines. 
-> Without it, developers would have to manually install matching versions of PostgreSQL, manually compile and install the pgvector extension, and resolve OS-specific dependency conflicts. 
-> It also keeps the host OS clean of background database services when not actively developing.

How will i know it's working?
-> Checking the container status (docker ps | grep pgvector) and successfully establishing a connection to the database from the host machine using psql -h localhost -p 5532 -U ai and executing a basic query like SELECT version();


About pg_vector.sh

docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql \
  -v pgvolume:/var/lib/postgresql \
  -p 5532:5432 \
  --name pgvector \
  agnohq/pgvector:18


1. docker run -d \: Instructs Docker to create and start a new container in "detached" mode (-d), meaning it will run in the background and free up the terminal.

2. -e POSTGRES_DB=ai \: Sets an environment variable to automatically create a default database named ai on first startup.

3. -e POSTGRES_USER=ai \: Sets an environment variable assigning ai as the superuser username.

4. -e POSTGRES_PASSWORD=ai \: Sets an environment variable assigning ai as the password for the superuser.

5. -e PGDATA=/var/lib/postgresql \: Sets the environment variable telling the Postgres process exactly which directory inside the container to use for writing database files.

6. -v pgvolume:/var/lib/postgresql \: Mounts a Docker managed "named volume" called pgvolume to the /var/lib/postgresql path inside the container. What this means for data: This ensures database persistence. Even if the container is destroyed, the data remains safely stored on the host in pgvolume and will be reattached to any future container using this same volume name.

7. -p 5532:5432 \: Maps port 5532 on the host machine to port 5432 (the default Postgres port) inside the container. You must connect to 5532 from the host.

8. --name pgvector \: Assigns the human-readable name pgvector to the container, so it can be referenced easily in commands like docker stop pgvector instead of using a random container ID.

9. agnohq/pgvector:18: Specifies the exact image and tag (version 18) to use as the blueprint for the container.

