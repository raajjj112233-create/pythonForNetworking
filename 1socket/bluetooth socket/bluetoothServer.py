import socket

# Define communication channel (similar to ports in standard TCP/IP)
BT_CHANNEL = 1  

def start_bluetooth_server():
    # 1. Create an RFCOMM Bluetooth socket
    server_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    
    try:
        # 2. Bind the socket to the chosen channel using the universal address
        server_socket.bind(("00:00:00:00:00:00", BT_CHANNEL))
        
        # 3. Start listening for incoming connections (queue up to 1 connection)
        server_socket.listen(1)
        print(f"Server is listening for connections on RFCOMM channel {BT_CHANNEL}...")
        
        # 4. Accept a connection request from a client device
        client_socket, client_info = server_socket.accept()
        print(f"Successfully connected to client at MAC address: {client_info[0]}")
        
        # 5. Receive incoming data payloads from the client
        while True:
            data = client_socket.recv(1024)  # Receive buffer size 1024 bytes
            if not data:
                break  # Exit loop if the client closes the connection cleanly
                
            message = data.decode("utf-8")
            print(f"Received message: {message}")
            
            # Echo response back to the client
            client_socket.send(f"Echo: {message}".encode("utf-8"))
            
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        # 6. Ensure clean resource cleanup upon termination
        if 'client_socket' in locals():
            client_socket.close()
        server_socket.close()
        print("Sockets closed. Server stopped.")

if __name__ == "__main__":
    start_bluetooth_server()
