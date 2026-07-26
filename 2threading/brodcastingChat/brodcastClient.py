import socket
import threading

client = socket.socket()

client.connect(("127.0.0.1", 5000))

name = input("Enter your name: ")


def receive():

    while True:

        try:

            message = client.recv(1024)

            print(message.decode())

        except:
            break


def send():

    while True:

        msg = input()

        full_msg = f"{name}: {msg}"

        client.send(full_msg.encode())


threading.Thread(target=receive).start()

threading.Thread(target=send).start()