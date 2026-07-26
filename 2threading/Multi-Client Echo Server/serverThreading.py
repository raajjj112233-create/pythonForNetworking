import socket
import threading


def handle_client(client, addr):

    print("Connected:", addr)

    while True:

        data = client.recv(1024)

        if not data:
            break

        print(addr, "says:", data.decode())

        client.send(data)

    client.close()

    print("Disconnected:", addr)


server = socket.socket()

server.bind(("0.0.0.0", 5000))

server.listen()

print("Server Started")


while True:

    client, addr = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(client, addr)
    )

    thread.start()