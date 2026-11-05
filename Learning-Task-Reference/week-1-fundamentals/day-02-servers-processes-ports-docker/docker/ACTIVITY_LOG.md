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