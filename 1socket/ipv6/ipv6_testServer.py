import socket

# Bind to all available interfaces (IPv4 and IPv6)
HOST = '::'  
PORT = 50007

# Create an IPv6 socket
with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
    # Crucial step: Allow dual-stack (IPv4 + IPv6) connections on this socket
    s.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
    
    s.bind((HOST, PORT))
    s.listen()
    print(f"Dual-Stack Server listening on all interfaces at port {PORT}...")
    print("Ready to accept both IPv4 and IPv6 connections from your hotspot.")
    
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected successfully by client: {addr}")
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received message: {data.decode()}")
            conn.sendall(b"Hello from the Dual-Stack Server!")
