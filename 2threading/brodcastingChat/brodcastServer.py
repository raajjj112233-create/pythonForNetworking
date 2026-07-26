import socket
import threading

clients = []

def broadcast(message, sender):

    for client in clients:

        if client != sender:

            try:
                client.send(message)

            except:
                clients.remove(client)


def handle_client(client):

    while True:

        try:

            message = client.recv(1024)

            if not message:
                break

            broadcast(message, client)

        except:
            break

    clients.remove(client)

    client.close()


server = socket.socket()

server.bind(("0.0.0.0", 5000))

server.listen()

print("Chat Server Started")

while True:

    client, addr = server.accept()

    print("Connected:", addr)

    clients.append(client)

    thread = threading.Thread(
        target=handle_client,
        args=(client,)
    )

    thread.start()