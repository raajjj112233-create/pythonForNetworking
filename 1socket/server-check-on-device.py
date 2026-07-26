import socket
import sys

# Define the target (use localhost/127.0.0.1 for safe, local testing)
TARGET_HOST = "127.0.0.1"

# Define a short list of common infrastructure ports to scan
# 22: SSH, 80: HTTP, 443: HTTPS, 3306: MySQL, 8080: Web Alt
PORTS_TO_SCAN = list(range(1, 70000))

print(f"Starting localized scan on host: {TARGET_HOST}")
print("-" * 50)

try:
    for port in PORTS_TO_SCAN:
        # Initialize an IPv4 TCP socket
        # The 'with' statement ensures the socket closes after every iteration
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as scan_socket:
            
            # Set a 1.0 second timeout so the script doesn't freeze on blocked ports
            scan_socket.settimeout(1.0)
            
            # Attempt the connection
            result = scan_socket.connect_ex((TARGET_HOST, port))
            
            if result == 0:
                print(f"Port {port}: OPEN")
            else:
                continue

except KeyboardInterrupt:
    print("\nScan terminated by user.")
    sys.exit()

except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()

except socket.error:
    print("\nCould not connect to the server environment.")
    sys.exit()
