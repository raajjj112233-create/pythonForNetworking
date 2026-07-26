import socket

TARGET_HOST = "127.0.0.1"
PORT = 22  # SSH port is highly prone to sending detailed text banners

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as net_socket:
    net_socket.settimeout(2.0)
    
    # Check if the port is open first
    if net_socket.connect_ex((TARGET_HOST, PORT)) == 0:
        print(f"Port {PORT} is OPEN. Attempting to read service banner...")
        
        try:
            # Read the first 1024 bytes of data sent automatically by the service
            banner = net_socket.recv(1024)
            print(f"Service Banner: {banner.decode().strip()}")
        except socket.timeout:
            print("Port opened, but the service did not send a banner within the timeout window.")
