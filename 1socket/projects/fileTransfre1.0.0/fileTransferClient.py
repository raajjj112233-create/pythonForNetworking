import socket


    
while True:


    file_name = input("Enter the name of the file to send: ")
    
    client = socket.socket()

    client.connect(("127.0.0.1", 5000))

    client.send(file_name.encode())

    file = open(file_name, "rb")

    while True:

        data = file.read(1024)

        if not data:
            break

        client.send(data)

    file.close()
    client.close()

    print("File sent successfully!")