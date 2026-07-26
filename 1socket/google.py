import socket

s = socket.socket()

s.connect(("google.com", 80))

s.send(
    b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n"
)

data = s.recv(4096)

print(data.decode(errors="ignore"))

s.close()