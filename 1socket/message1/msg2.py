


import socket
import threading

DISCOVERY_IP = "127.0.0.1"
DISCOVERY_PORT = 5000

MY_ID = input("Enter your ID: ")
MY_PORT = int(input("Enter your listening port: "))

chat_socket = None


# -------------------------
# Peer chat server
# -------------------------
def peer_server():
    global chat_socket

    server = socket.socket()
    server.bind(("0.0.0.0", MY_PORT))
    server.listen(1)

    print(f"Listening for chats on port {MY_PORT}")

    conn, addr = server.accept()

    print(f"\nChat connected from {addr}")

    chat_socket = conn

    receive_messages(conn)


# -------------------------
# Receive messages
# -------------------------
def receive_messages(conn):

    while True:
        try:
            data = conn.recv(1024)

            if not data:
                break

            print(f"\nFriend: {data.decode()}")

        except:
            break


# -------------------------
# Register with discovery
# -------------------------
s = socket.socket()
s.connect((DISCOVERY_IP, DISCOVERY_PORT))

s.send(
    f"REGISTER {MY_ID} {MY_PORT}".encode()
)

print("Discovery:", s.recv(1024).decode())

s.close()


# -------------------------
# Start peer server
# -------------------------
threading.Thread(
    target=peer_server,
    daemon=True
).start()


# -------------------------
# Find peer
# -------------------------
target_id = input("Peer ID to connect: ")

s = socket.socket()
s.connect((DISCOVERY_IP, DISCOVERY_PORT))

s.send(
    f"FIND {target_id}".encode()
)

reply = s.recv(1024).decode()

s.close()

print("Discovery:", reply)

# -------------------------
# Connect to peer
# -------------------------
if reply.startswith("FOUND"):

    _, ip, port = reply.split()

    try:

        peer = socket.socket()
        peer.connect((ip, int(port)))

        chat_socket = peer

        threading.Thread(
            target=receive_messages,
            args=(peer,),
            daemon=True
        ).start()

        print("Connected to peer!")

    except:

        print("Peer not accepting connections yet.")

else:

    print("Peer not found.")


# -------------------------
# Chat loop
# -------------------------
while True:

    if chat_socket is None:
        continue

    msg = input("You: ")

    try:
        chat_socket.send(msg.encode())

    except:
        print("Connection lost")
        break