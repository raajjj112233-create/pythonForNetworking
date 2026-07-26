import socket

server = socket.socket()

server.bind(("0.0.0.0", 5000))
server.listen()

print("Waiting for file...")

while True:



    client, addr = server.accept()

    message = client.recv(1024)
    
    file_name = message.decode()

    file = open(file_name, "wb")

    while True:

        data = client.recv(1024)

        if not data:
            break

        file.write(data)

    file.close()
    client.close()

    print("File received successfully!")