import socket

HOST = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"HTTP server running at http://{HOST}:{PORT}")

while True:
    conn, addr = server.accept()

    request = conn.recv(1024).decode()
    print("REQUEST:\n", request)

    response = """HTTP/1.1 200 OK

Hello from raw Python HTTP server
"""

    conn.send(response.encode())
    conn.close()
