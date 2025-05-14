# BaseHTTPRequestHandler handles the incoming HTTP requests, defines how your server
# HTTPServer creates a basic server.
# JSON helps us send/receive JSON data (API format)

from http.server import BaseHTTPRequestHandler, HTTPServer
import json




class SimpleAPIHandler(BaseHTTPRequestHandler):
    # a method that will be called when the server receives a GET request
    def do_GET(self):
        try:
            if self.path == "/":
                self.send_response(200)
                # Adds a header to tell the client what kind of data is coming (Content-Type) and whether the request was successful {status code}
                self.send_header("Content-Type", "application/json")
                # Ends the header section so that you can now send the actual response body.
                self.end_headers()
                response = {"message": "Hello! This is a GET request"}
                # .encode(): Converts the string to bytes because wfile.write() needs bytes.
                # self.wfile is like a pipe that sends data back to the client.
                self.wfile.write(json.dumps(response).encode())
            else:
                self.send_error(404, "Path not found")
        except Exception as e:
            # str(e) returns the error message into a readable strings.
            self.send_error(500, f"Internal Server Error: {str(e)}")


    def do_POST(self):
        try:
            if self.path == "/data":
                # content_length will be an integer representing how many bytes of data were sent in
                content_length = int(self.headers.get("Content-Length", 0))
                post_data = self.rfile.read(content_length)

                try:
                    data = json.loads(post_data)
                    # if the JSON string you want to convert to python dictionary is badly formatted

                except json.JSONDecodeError:
                    self.send_error(400, "Invalid JSON format")
                    return

                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                # This is called an echo response, often used for testing or confirming receipt of
                response = {"received": data}
                self.wfile.write(json.dumps(response).encode())
            else:
                self.send_error(404, "Path not found")
        except Exception as e:
            self.send_error(500, f"Internal Server Error: {str(e)}")


# The "" means it listens on all available IP addresses (like localhost).
# 8000 is the port number. You'll access your server at http://localhost:8000
server_address = ("", 8000)
httpd = HTTPServer(server_address, SimpleAPIHandler)
print("Server is running on http://localhost:8000")

# Starts the server loop
httpd.serve_forever()




