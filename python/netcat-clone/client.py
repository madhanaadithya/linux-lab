import socket

HOST = "127.0.0.1"
PORT = 9000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

client.send("Hello from client".encode())

response = client.recv(1024).decode()
print("Server replied:", response)

client.close()
