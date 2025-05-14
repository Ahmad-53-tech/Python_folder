import socket



client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("127.0.0.1", 12345))

delivered = "Hello Server"

message = client_socket.send(delivered.encode())

received = client_socket.recv(1024)

print("Message from server:", received)

client_socket.close()

