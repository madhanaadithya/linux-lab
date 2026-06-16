import socket

HOST = "127.0.0.1"
PORT = 9000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Server listening on {HOST}:{PORT}")

conn, addr = server.accept()
print("Connected by", addr)

data = conn.recv(1024).decode()
print("Client says:", data)

conn.send("Hello from server".encode())

conn.close()
server.close()
