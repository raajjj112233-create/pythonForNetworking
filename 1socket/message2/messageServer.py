import socket
import threading

HOST = "0.0.0.0"
PORT = 5000

server = socket.socket()
server.bind((HOST, PORT))
server.listen()

print("Server started on port", PORT)

def handle_client(client, addr):

    print("Connected:", addr)

    while True:

        try:
            data = client.recv(1024)

            if not data:
                break

            message = data.decode()

            print(f"{addr}: {message}")

            client.send(
                f"Server received: {message}".encode()
            )

        except:
            break

    print("Disconnected:", addr)

    client.close()

while True:

    client, addr = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(client, addr)
    )

    thread.start()