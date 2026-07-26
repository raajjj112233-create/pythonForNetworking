import socket

HOST = "10.41.50.248"
PORT = 5000

while True:

    client = socket.socket()

    client.connect((HOST, PORT))

    print("\n=== CLIENT INFO ===")
    print("My Address     :", client.getsockname())
    print("Server Address :", client.getpeername())

    send = input("\nyou: ")
    message = "from client2: " + send

    client.send(message.encode())

    print("\n=== MESSAGE SENT ===")
    print("Sender  :", client.getsockname())
    print("Receiver:", client.getpeername())
    print("Message :", message)

    reply = client.recv(1024)

    print("\n=== MESSAGE RECEIVED ===")
    print("Sender  :", client.getpeername())
    print("Receiver:", client.getsockname())
    print("Message :", reply.decode())

    client.close()