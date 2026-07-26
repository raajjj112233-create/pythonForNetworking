import socket

# Define host (all interfaces) and port
HOST = '::' 
PORT = 50007

# Create an IPv6 TCP socket
with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Server listening on [{HOST}]:{PORT}...")
    
    # Wait for a connection
    conn, addr = s.accept()
    with conn:
        print(f"Connected successfully by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode()}")
            conn.sendall(b"Message received by server!")
