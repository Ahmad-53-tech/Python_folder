# Build a mini API server for a full delivery app called snack swift, your job is to set up a basic python server that can:
# * 1. Return a list of available food items
# * 2. Accept and store a new order.
# * 3. Handle simple error for bad request or wrong path using python built in http.server module:
# - Create a class Snack Swift API Handler.
# - Implement these two end points (GET/Menu: This should respond with a JSON array of food items (Burger, Fries & Soda) and prices.
# Post/Order: This should accept data in JSON data { "item": "Burger", "Quantity": 2}
# - Validate the data then return "Order received for 2 Burger(s)"
# - Handle errors.

from http.server import BaseHTTPRequestHandler, HTTPServer
import json



class SnackSwiftAPIHandler(BaseHTTPRequestHandler):
    menu = [
        {"item": "burger", "price": 4.99},
        {"item": "Fries", "price": 5.99},
        {"item": "Soda", "price": 3.99}
    ]

    orders = []

    def do_GET(self):
        try:
            if self.path == "/menu":
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(self.menu).encode())
            else:
                self.send_error(404, "Path not found")
        except Exception as e:
            self.send_error(500, f"Internal Server Error: {str(e)}")

    def do_POST(self):
        try:
            if self.path == "/order":
                content_length = int(self.headers.get("Content-Length", 0))
                post_data = self.rfile.read(content_length)

                try:
                    data = json.loads(post_data)
                except json.JSONDecodeError:
                    self.send_error(400, "Invalid JSON format")
                    return

                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                quantity = data.get("quantity")
                item = data.get("item")
                response = {f"Order received for {quantity} {item}"}
                self.wfile.write(json.dumps(response).encode())


            else:
                self.send_error(404, "Path not found")
        except Exception as e:
            self.send_error(500, f"Internal Server Error: {str(e)}")



server_address = ("", 8000)
httpd = HTTPServer(server_address, SnackSwiftAPIHandler)
print("Server is running on http://localhost:8000")

httpd.serve_forever()



