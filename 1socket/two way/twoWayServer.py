import socket

server = socket.socket()

server.bind(("0.0.0.0", 5000))

server.listen(1)

print("Waiting for connection...")

client, address = server.accept()

print("Connected by:", address)

message = client.recv(1024)

print("Client says:", message.decode())

client.send(b"Message received:- " + message)

client.close()
server.close()