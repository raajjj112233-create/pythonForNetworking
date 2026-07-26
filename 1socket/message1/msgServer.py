import socket

HOST = "0.0.0.0"
PORT = 5000

peers = {}

server = socket.socket()
server.bind((HOST, PORT))
server.listen()

print("Discovery Server Running...")
print(f"Listening on {HOST}:{PORT}")

while True:

    conn, addr = server.accept()

    try:

        data = conn.recv(1024).decode()

        if not data:
            conn.close()
            continue

        print("\nReceived:", data)

        parts = data.split()

        if parts[0] == "REGISTER":

            peer_id = parts[1]
            peer_port = parts[2]

            peers[peer_id] = (addr[0], peer_port)

            print(f"Registered {peer_id} -> {addr[0]}:{peer_port}")

            conn.send(b"REGISTERED")

        elif parts[0] == "FIND":

            target_id = parts[1]

            if target_id in peers:

                ip, port = peers[target_id]

                reply = f"FOUND {ip} {port}"

                conn.send(reply.encode())

                print("Sent:", reply)

            else:

                conn.send(b"NOT_FOUND")

                print("Peer not found")

        else:

            conn.send(b"INVALID_COMMAND")

    except Exception as e:

        print("Error:", e)

    conn.close()
    