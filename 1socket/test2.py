import socket

s = socket.socket()

s.connect(("example.com", 80))

print("Connected!")

s.close()

print("Connection Closed!")