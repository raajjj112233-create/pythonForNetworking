# Python Sockets Guide

A socket is an endpoint for communication between two devices over a network.

Sockets allow programs to:

- Send and receive data
- Build chat applications
- Create web servers
- Transfer files
- Develop multiplayer games
- Build network tools

---

# What is a Socket?

Think of a socket as a communication channel.

Example:

```text
Client  <--------->  Server
```

The client connects to the server using:

```text
IP Address + Port Number
```

Example:

```text
192.168.1.10:5000
```

---

# Socket Types

## TCP Socket

TCP provides:

- Reliable communication
- Error checking
- Ordered delivery
- Connection-oriented communication

Example uses:

- Websites (HTTP/HTTPS)
- File transfers
- Email
- Chat applications

Python:

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

---

## UDP Socket

UDP provides:

- Fast communication
- No connection setup
- No delivery guarantee
- Lower overhead

Example uses:

- Video streaming
- Online gaming
- VoIP
- DNS

Python:

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

---

# Socket Components

## IP Address

Identifies a device on the network.

Examples:

```text
127.0.0.1
192.168.1.100
8.8.8.8
```

---

## Port Number

Identifies a specific service.

Examples:

| Service | Port |
|----------|--------|
| HTTP | 80 |
| HTTPS | 443 |
| SSH | 22 |
| FTP | 21 |
| Custom Server | 5000 |

---

# Common Socket Functions

## socket()

Creates a socket.

```python
server = socket.socket()
```

---

## bind()

Attaches a socket to an IP and port.

```python
server.bind(("0.0.0.0", 5000))
```

Meaning:

```text
0.0.0.0 = Listen on all interfaces
5000    = Port number
```

---

## listen()

Waits for incoming connections.

```python
server.listen()
```

---

## accept()

Accepts a client connection.

```python
client, address = server.accept()
```

Example:

```text
Client IP: 192.168.1.20
Client Port: 50234
```

---

## connect()

Connects to a remote server.

```python
client.connect(("127.0.0.1", 5000))
```

---

## send()

Sends data.

```python
client.send(b"Hello")
```

---

## recv()

Receives data.

```python
data = client.recv(1024)
```

Meaning:

```text
Receive up to 1024 bytes
```

---

## close()

Closes a socket.

```python
client.close()
```

---

# TCP Echo Server Example

## Server

```python
import socket

server = socket.socket()

server.bind(("0.0.0.0", 5000))
server.listen()

print("Waiting for connection...")

client, address = server.accept()

print("Connected:", address)

message = client.recv(1024)

print("Received:", message.decode())

client.send(message)

client.close()
server.close()
```

---

## Client

```python
import socket

client = socket.socket()

client.connect(("127.0.0.1", 5000))

client.send(b"Hello Server")

reply = client.recv(1024)

print("Server:", reply.decode())

client.close()
```

---

# Data Encoding

Sockets transmit bytes.

Convert text to bytes:

```python
message = "Hello"

message.encode()
```

Convert bytes to text:

```python
data.decode()
```

---

# TCP Communication Flow

```text
1. Server creates socket
2. Server binds IP and port
3. Server listens
4. Client creates socket
5. Client connects
6. Data exchanged
7. Connection closed
```

Diagram:

```text
Client                     Server
  |                           |
  |------ connect() --------->|
  |                           |
  |-------- send() ---------->|
  |                           |
  |<------- recv() -----------|
  |                           |
  |------- close() ---------->|
```

---

# UDP Example

## UDP Server

```python
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("0.0.0.0", 5000))

while True:
    data, addr = server.recvfrom(1024)

    print("Received:", data.decode())

    server.sendto(b"Message Received", addr)
```

---

## UDP Client

```python
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"Hello UDP", ("127.0.0.1", 5000))

reply, addr = client.recvfrom(1024)

print(reply.decode())
```

---

# File Transfer Concept

```text
Sender
   |
Read File
   |
Convert to Bytes
   |
Send Through Socket
   |
Receiver
   |
Receive Bytes
   |
Write to File
```

Basic sending:

```python
with open("file.txt", "rb") as f:
    data = f.read()

client.send(data)
```

Receiving:

```python
data = client.recv(4096)

with open("received.txt", "wb") as f:
    f.write(data)
```

---

# Socket Address Families

## IPv4

```python
socket.AF_INET
```

Example:

```text
192.168.1.10
```

---

## IPv6

```python
socket.AF_INET6
```

Example:

```text
2405:201:abcd::1234
```

---

# Socket Constants

| Constant | Meaning |
|-----------|-----------|
| AF_INET | IPv4 |
| AF_INET6 | IPv6 |
| SOCK_STREAM | TCP |
| SOCK_DGRAM | UDP |

---

# Useful Commands

## Linux

View listening ports:

```bash
ss -tuln
```

or

```bash
netstat -tuln
```

---

Check active connections:

```bash
ss -ant
```

---

## Windows

```cmd
netstat -ano
```

---

# Common Errors

## Address Already in Use

```text
OSError: [Errno 98] Address already in use
```

Fix:

```python
server.setsockopt(
    socket.SOL_SOCKET,
    socket.SO_REUSEADDR,
    1
)
```

---

## Connection Refused

```text
ConnectionRefusedError
```

Possible causes:

- Server not running
- Wrong IP
- Wrong port
- Firewall blocking connection

---

## Timeout

```text
socket.timeout
```

Set timeout:

```python
client.settimeout(5)
```

---

# Learning Roadmap

1. TCP Client
2. TCP Server
3. Multi-Client Server
4. Threading
5. UDP Communication
6. File Transfer
7. Chat Application
8. IPv6 Sockets
9. Network Discovery
10. HTTP Server
11. Port Scanner (authorized systems only)
12. Secure Communication (SSL/TLS)

---

# References

Python Socket Module:

```python
import socket
```

Official Documentation:

https://docs.python.org/3/library/socket.html
