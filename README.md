# Socket & Threading Learning Repository

Welcome to the **Socket & Threading Learning Repository**.

This repository contains practical examples, notes, and projects for learning:

- Python Networking
- TCP Sockets
- UDP Sockets
- Multi-Client Servers
- Threading
- Concurrent Network Programming
- File Transfer
- Chat Applications

---

# Repository Structure

```text
Socket-And-Threading/
│
├── README.md
│
├── sockets/
│   ├── README.md
│   ├── tcp/
│   │   ├── server.py
│   │   └── client.py
│   │
│   ├── udp/
│   │   ├── udp_server.py
│   │   └── udp_client.py
│   │
│   └── file_transfer/
│       ├── sender.py
│       └── receiver.py
│
├── threading/
│   ├── README.md
│   ├── basics/
│   │   ├── thread_example.py
│   │   └── multiple_threads.py
│   │
│   └── networking/
│       ├── threaded_server.py
│       └── threaded_chat.py
│
└── projects/
    ├── chat_application/
    ├── multi_client_server/
    └── network_tools/
```

---

# Available Documentation

## Socket Documentation

Navigate to:

```text
sockets/README.md
```

Topics covered:

- What is a Socket?
- TCP Communication
- UDP Communication
- Client and Server Architecture
- Socket Functions
- File Transfer
- IPv4 and IPv6 Sockets
- Common Networking Errors

---

## Threading Documentation

Navigate to:

```text
threading/README.md
```

Topics covered:

- What is a Thread?
- Why Threading is Needed
- Creating Threads
- Multiple Threads
- Daemon Threads
- Thread Synchronization
- Locks and Race Conditions
- Threading in Network Servers

---

# Learning Path

Follow the topics in this order:

### Phase 1: Python Basics

- Variables
- Loops
- Functions
- Files
- Modules

---

### Phase 2: Networking Fundamentals

- IP Address
- MAC Address
- Ports
- Protocols
- TCP
- UDP

---

### Phase 3: Socket Programming

Navigate to:

```text
sockets/README.md
```

Learn:

1. Socket Creation
2. Binding
3. Listening
4. Accepting Connections
5. Sending Data
6. Receiving Data
7. Closing Connections

---

### Phase 4: Threading

Navigate to:

```text
threading/README.md
```

Learn:

1. Thread Creation
2. Starting Threads
3. Joining Threads
4. Multiple Threads
5. Shared Resources
6. Locks

---

### Phase 5: Combining Sockets and Threads

Learn how to:

- Handle multiple clients
- Create chat applications
- Build concurrent servers
- Process requests simultaneously

Example:

```text
Client 1 ── Thread 1
Client 2 ── Thread 2
Client 3 ── Thread 3
Client 4 ── Thread 4
               │
               ▼
            Server
```

---

# Recommended Study Order

```text
1. TCP Socket
2. UDP Socket
3. File Transfer
4. Thread Basics
5. Multiple Threads
6. Threaded TCP Server
7. Multi-Client Chat
8. Network Discovery
9. Advanced Networking Projects
```

---

# Example Commands

Run a TCP server:

```bash
python server.py
```

Run a TCP client:

```bash
python client.py
```

Run a threaded server:

```bash
python threaded_server.py
```

---

# Goals of This Repository

By completing this repository you should be able to:

- Understand networking fundamentals
- Build TCP and UDP applications
- Create multi-client servers
- Use threads effectively
- Develop network-based tools
- Design scalable networking projects

---

# Documentation Index

| Topic | File |
|---------|---------|
| Socket Programming | sockets/README.md |
| Threading | threading/README.md |
| TCP Examples | sockets/tcp/ |
| UDP Examples | sockets/udp/ |
| File Transfer | sockets/file_transfer/ |
| Thread Basics | threading/basics/ |
| Network Threading | threading/networking/ |

---

# Next Steps

Open the following files in order:

```text
1. sockets/README.md
2. threading/README.md
3. sockets/tcp/server.py
4. sockets/tcp/client.py
5. threading/networking/threaded_server.py
```

Happy Learning and Happy Coding!
