import socket
import os



while True:

    FILE_NAME = input("Enter the file name to send: ")

    client = socket.socket()

    client.connect(("10.41.50.193", 5000))

    # Send filename
    client.send(FILE_NAME.encode())

    client.recv(1024)

    # Get file size
    filesize = os.path.getsize(FILE_NAME)

    # Send file size
    client.send(str(filesize).encode())

    client.recv(1024)

    # Send file data
    with open(FILE_NAME, "rb") as file:

        while True:

            data = file.read(1024)

            if not data:
                break

            client.send(data)

    print("File sent successfully!")

    client.close()