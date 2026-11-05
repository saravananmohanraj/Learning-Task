About Processes and ports
-> Processes are active, running instance of programs on our computer, each tracked by the unique number (PID)
-> Ports are designated digital endpoints that processes use to send and receive the incoming traffic.

Flow
1. When you start a server, the operating system registers it as a process. 
2. That process then asks the OS to reserve a specific port to listen for incoming traffic.

Eg:

[ Incoming Request (e.g., web traffic) ] 
          │
          ▼
[ Operating System (Network Interface) ]
          
        1.    Traffic for Port 80   ──> Process A (PID 1024: Nginx Web Server)
          
        2.    Traffic for Port 5432 ──> Process B (PID 2048: PostgreSQL Database)
          
        3.    Traffic for Port 8000 ──> Process C (PID 4096: Your Python Server)


Why?
-> Without processes, your computer could only run one program at a time. 
-> Without ports, your computer wouldn't know where to send incoming network data. 
-> If an email and a web page arrived at the same time, the OS wouldn't know which application should handle which piece of data, resulting in total network chaos.

How will i know it's working?
-> A process is working if it appears in the system's process list with a healthy status. 
-> A port binding is working if you can see the process actively "LISTENING" on that port using network diagnostic tools.
-> If you can successfully send a request to that port (like opening http://localhost:8000 in a browser) and get a response.

Core concepts:
Process (PID): A Process ID is a unique numerical identifier assigned by the OS to every running program. It is the system's way of tracking and managing that program's resource usage.

Port: A logical channel that directs network traffic to a specific process.

Listening: When a process is "listening," it has successfully bound to a port and is actively waiting in the background for incoming connections or data.

Commands:

saravanan_3340@DESKTOP-G2PRDKV:~$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...

saravanan_3340@DESKTOP-G2PRDKV:~$ lsof -i :8000
COMMAND  PID           USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
python3 3710 saravanan_3340    3u  IPv4  93928      0t0  TCP *:8000 (LISTEN)

saravanan_3340@DESKTOP-G2PRDKV:~$ kill 3710

saravanan_3340@DESKTOP-G2PRDKV:~$ python3 -m http.server 8000
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
Terminated

saravanan_3340@DESKTOP-G2PRDKV:~$ ps aux | grep node
root         129  0.0  0.0 152948  1556 ?        Ssl  07:36   0:00 snapfuse /var/lib/snapd/snaps/core20_2769.snap /snap/core20/2769 -o ro,nodev,allow_other,suid
root         134  0.0  0.0 152948  1812 ?        Ssl  07:36   0:00 snapfuse /var/lib/snapd/snaps/core20_2922.snap /snap/core20/2922 -o ro,nodev,allow_other,suid
root         137  0.0  0.0 152948  1556 ?        Ssl  07:36   0:00 snapfuse /var/lib/snapd/snaps/snapd_25577.snap /snap/snapd/25577 -o ro,nodev,allow_other,suid
root         143  0.0  0.0 227844  1908 ?        Ssl  07:36   0:00 snapfuse /var/lib/snapd/snaps/snapd_26865.snap /snap/snapd/26865 -o ro,nodev,allow_other,suid
saravan+    3776  0.0  0.0   4104  2168 pts/4    S+   10:52   0:00 grep --color=auto node

saravanan_3340@DESKTOP-G2PRDKV:~$ lsof -i -P -n | grep LISTEN
python3 3848 saravanan_3340    3u  IPv4  96746      0t0  TCP *:8000 (LISTEN)


kill vs kill -9:
kill (Signal 15): Politely asks a process to clean up and shut down.
kill -9 (Signal 9): Forces the OS to terminate the process immediately without cleanup.


Faced issue:
Tried to run lsof and ps in standard Windows Command Prompt, but they threw "command not found" errors because they are Linux-specific commands. 
netstat caused confusion with CLOSED and TIME_WAIT states when trying to run everything in a single window.

Switched to WSL (Ubuntu) to use the proper native Linux networking and process tools as intended by the guide, and utilized two separate terminal tabs to keep the server running while diagnosing it.