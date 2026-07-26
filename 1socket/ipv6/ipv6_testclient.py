import socket

# Define host (IPv6 local loopback) and port
HOST = '::1'
PORT = 50007

# Create an IPv6 TCP socket
with socket.socket(socket.AF_INET6, socket.SOCK_STREAM) as s:
    print(f"Connecting to [{HOST}]:{PORT}...")
    s.connect((HOST, PORT, 0, 0)) # 4-tuple format for AF_INET6
    
    # Send test data
    s.sendall(b"Hello IPv6 Server!")
    data = s.recv(1024)

print(f"Server response: {data.decode()}")
