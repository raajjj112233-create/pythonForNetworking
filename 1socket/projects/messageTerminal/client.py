import socket

while True:

    client = socket.socket()

    client.connect(("127.0.0.1", 6000))


    message = input("Enter your message: ")

    client.send(message.encode())

    reply = client.recv(1024)

    print("Server echo:", reply.decode())

    client.close()

    