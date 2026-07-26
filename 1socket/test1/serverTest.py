import socket

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket()

server.bind((HOST, PORT))

server.listen(2)

print("Server started")
print("Listening on port:", PORT)

while True:

    client, addr = server.accept()

    print("\n=== CLIENT CONNECTED ===")
    print("Client Address:", addr)

    print("\n=== SERVER ADDRESS ===")
    print(client.getsockname())

    data = client.recv(1024)

    print("\n=== MESSAGE RECEIVED ===")
    print("Sender  :", addr)
    print("Receiver:", client.getsockname())
    print("Message", data.decode())
    request = data.decode()


  

    reply = input("\nReply: ")

    client.send(reply.encode())

    print("\n=== MESSAGE SENT ===")
    print("Sender  :", client.getsockname())
    print("Receiver:", addr)
    print("Message :", reply)

   