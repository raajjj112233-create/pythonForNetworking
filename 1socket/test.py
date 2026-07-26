import socket

s = socket.socket()

s.connect(("google.com", 80))

s.send(
    b"GET / HTTPS/1.1\r\nHost: google.com\r\n\r\n"
)

while True:
    data = s.recv(1024)

    if not data:
        break
    print(data)


s.close()