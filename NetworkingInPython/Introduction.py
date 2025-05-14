#                                           NETWORKING IN PYTHON
#       Networking in python allows computers to communicate with each other over the internet or a local network.
#It enables data sharing, remote access, and web development.




#                             Python provides builtin libraries for networking. E.g.,
#1 - SOCKET: they are for low level network programming. They give you direct control over network communication without the abstractions
#of higher level protocols.

#2 - REQUESTS: they are for making http(hyper text transfer protocol) request.

#3 - URLLIB: it is used for handling URLs and web dater





#                                            The BASICS OF SOCKET
#       Sockets allow computers to send and receive data over a network. A socket is like a phone line, one service dives or connects to
#another. They send and receive messages. The connection is closed when done.





#                                   CREATING A SIMPLE SERVER AND CLIENT USING SOCKET


#           💎SERVER CODE (listens for connections from a client)


import socket
import requests
import urllib.request

# socket.socket(...) creates a socket (a communication end point). These endpoints allow them to exchange data.
#Socket.AF_INET specifies that we are using IPv4.
#Tcp (transmission communication protocol)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# .bind((IP, Port)) attaches the socket to an IP address (127.0.0.1, which is localhost) and a port number (12345).
# The Server will listen for connections on this IP and port.
server_socket.bind(("127.0.0.1", 12345))   # Bind to IP and port


# listen(1) makes the server wait for connections.
# The 1 means it will only allow one client to connect at a time.
server_socket.listen(1) # listen for connections
print("Server is waiting for connection.....")


# .accept() pauses the program until a client connects.
# When a client connects, client_socket is the connection to the client and addr is a tuple with the client's IP address and port.
# The Server then prints who connected.
client_socket, addr = server_socket.accept()
print(f"Connected to {addr}")

# .send(b"...") sends bytes (b"..." means a byte message) to the client.
client_socket.send(b"Hello from server!") #Send a message


# .close() closes the connection to free up resources.
client_socket.close() #Close Connection
server_socket.close()



#           💎 Client Code (Connects to Server)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# .connect((IP, port)) tells the client to connect to the server at 127.0.0.1:12345.
client_socket.connect(("127.0.0.1", 12345)) # Connect to server.

# .recv(1024) waits to receive up to 1024 bytes of data from the server. The received data is stored in a message
message = client_socket.recv(1024) # Receive data

# message.decode() converts the bytes into a reusable string.
print("Message from server:", message.decode())

client_socket.close()




# USE OF REQUESTS
response = requests.get("https://api.github.com")
print(response.status_code) # 200 means success, 404 means not found, 403 means forbidden, 500 means Internal server error.
data = response.json() # Prints response as JSON - json() → Converts the response to readable data.
print(data["title"]) # to access data






# USE OF urllib
# .request is a built-in Python module that allows us to fetch data from the internet (like making a browser request).
url = "http://example.com" # This is the web address (URL) from which we want to retrieve data.
response = urllib.request.urlopen(url) # This is like when a web browser sends a request and waits for the webpage data.
html = response.read() #  read() reads the raw bytes of the response. HTML contains the entire HTML source code of example.com.

print(html.decode()) # Print the page content. .decode() converts to the binary response (bytes) into