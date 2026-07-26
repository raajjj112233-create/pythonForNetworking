import socket

client = socket.socket()

client.connect(("127.0.0.1", 5000))

client.send(b"Hello darling!")

reply = client.recv(1024)

print("Server says:", reply.decode())

client.close()