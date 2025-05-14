import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("127.0.0.1", 12345))

server_socket.listen(1)

print("Server is waiting for a connection....")

client_socket, addr = server_socket.accept()
print(f"Connected to {addr}")

message = client_socket.recv(1024).decode()

response = f"Message Received: {message}"
client_socket.send(response.encode())


server_socket.close()
client_socket.close()



