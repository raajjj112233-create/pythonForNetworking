import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket()

client.connect((HOST, PORT))

while True:

    msg = input("You: ")

    client.send(msg.encode())

    reply = client.recv(1024)

    print(reply.decode())
