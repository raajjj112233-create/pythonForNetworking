import socket

server = socket.socket()
server.bind(("0.0.0.0", 6000))
server.listen()

print("Server started")

 
while True:
        

    print("Waiting for connection...")

    client, address = server.accept()

    print("Connected by:", address)

    message = client.recv(1024)

    decoded_message = message.decode()

    print("Client says:", decoded_message)

    reply = input("Enter your reply: ")

    client.send(reply.encode())

    client.close()
    


    