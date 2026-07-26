import socket

# Target server parameters
# !!! REPLACE WITH YOUR SERVER'S ACTUAL BLUETOOTH MAC ADDRESS !!!
SERVER_MAC_ADDRESS = "08:3e:8e:4b:c8:12"  
BT_CHANNEL = 1  

def start_bluetooth_client():
    # 1. Create an RFCOMM Bluetooth socket
    client_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    
    try:
        # 2. Initiate a network connection to the server
        print(f"Attempting connection to {SERVER_MAC_ADDRESS} on channel {BT_CHANNEL}...")
        client_socket.connect((SERVER_MAC_ADDRESS, BT_CHANNEL))
        print("Connected successfully.")
        
        # 3. Handle data transmission
        message_to_send = "Hello Bluetooth Server!"
        client_socket.send(message_to_send.encode("utf-8"))
        print(f"Sent: {message_to_send}")
        
        # 4. Wait for and process the return response payload
        response = client_socket.recv(1024)
        print(f"Server Response: {response.decode('utf-8')}")
        
    except Exception as e:
        print(f"Connection failed: {e}")
        
    finally:
        # 5. Terminate the socket connection session cleanly
        client_socket.close()
        print("Client session disconnected.")

if __name__ == "__main__":
    start_bluetooth_client()
