import socket

client = socket.socket()

client.connect(("127.0.0.1", 5000))

while True:

    msg = input("Message: ")

    client.send(msg.encode())

    reply = client.recv(1024)

    print("Server:", reply.decode())