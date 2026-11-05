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