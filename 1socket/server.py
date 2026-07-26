import socket

server = socket.socket()

server.bind(("0.0.0.0", 5000))

server.listen(1)

print("Waiting for connection...")

client, address = server.accept()

print("Connected by:", address)

client.send(b"Hello from my server!")

client.close()
server.close()