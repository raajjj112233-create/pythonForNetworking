import socket
import os

server = socket.socket()

server.bind(("0.0.0.0", 5000))
server.listen()

print("Waiting for connection...")

while True:

    client, addr = server.accept()

    print("Connected:", addr)

    # Receive filename
    filename = client.recv(1024).decode()

    # Send acknowledgment
    client.send(b"OK")

    # Receive file size
    filesize = int(client.recv(1024).decode())

    # Send acknowledgment
    client.send(b"OK")

    print("Receiving:", filename)
    print("Size:", filesize, "bytes")

    received = 0

    with open(filename, "wb") as file:

        while received < filesize:

            data = client.recv(1024)

            if not data:
                break

            file.write(data)

            received += len(data)

            print(f"{received}/{filesize} bytes")

    print("File received successfully!")

    client.close()
    