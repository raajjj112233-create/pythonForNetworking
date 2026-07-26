import socket

client = socket.socket()

client.connect(("127.0.0.1", 5000))

data = client.recv(1024)

print(data.decode())

client.close()