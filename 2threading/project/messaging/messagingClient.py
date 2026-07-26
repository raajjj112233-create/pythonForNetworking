import socket
import threading

client = socket.socket()

client.connect(("127.0.0.1", 5000))

name = input("Enter username without spaces: ")

client.send(name.encode())


def receive():

    while True:

        try:

            message = client.recv(1024)

            print("\n" + message.decode())

        except:
            break


def send():

    while True:

        msg = input()

        if msg.startswith("/pm"):

            client.send(msg.encode())

        else:

            full_msg = f"{name}: {msg}"

            client.send(full_msg.encode())


threading.Thread(target=receive, daemon=True).start()

send()
