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
