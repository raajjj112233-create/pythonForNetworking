import socket
import threading

clients = []
usernames = {}


def get_client_by_name(name):

    for client, username in usernames.items():

        if username == name:
            return client

    return None

def broadcast(message, sender=None):

    for client in clients:

        if client != sender:

            try:
                client.send(message.encode())

            except:
                pass
        


def handle_client(client):

    username = usernames[client]

    while True:

        try:

            message = client.recv(1024)

            if not message:
                break

            text = message.decode()

            if text.startswith("/pm"):

                parts = text.split(" ", 2)

                if len(parts) < 3:
                    continue

                target_name = parts[1]

                private_message = parts[2]

                target_client = get_client_by_name(target_name)

                if target_client:

                    sender = usernames[client]

                    target_client.send(
                        f"[PM from {sender}] {private_message}".encode()
                    )

                else:

                    client.send(
                        f"User {target_name} not found".encode()
                    )

            else:

                broadcast(text, client)

        except:
            break

    clients.remove(client)

    del usernames[client]

    client.close()

    leave_msg = f"{username} left the chat"

    print(leave_msg)

    broadcast(leave_msg)


server = socket.socket()

server.bind(("0.0.0.0", 5000))

server.listen()

print("Chat Server Started")

while True:

    client, addr = server.accept()

    username = client.recv(1024).decode()

    clients.append(client)

    usernames[client] = username

    join_msg = f"{username} joined the chat"

    print(join_msg)

    broadcast(join_msg)

    thread = threading.Thread(
        target=handle_client,
        args=(client,)
    )

    thread.start()
