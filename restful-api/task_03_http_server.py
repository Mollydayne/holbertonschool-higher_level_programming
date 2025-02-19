#!/usr/bin/python3
"""
Task 3. Develop a simple API using Python
"""

from http.server import SimpleHTTPRequestHandler, HTTPServer
import json

class SimpleHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        routes = {
            "/": self.handle_home,
            "/data": self.handle_data,
            "/status": self.handle_status,
        }

        handler = routes.get(self.path, self.handle_404)
        handler()

    def handle_home(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")

    def handle_data(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        data = {"name": "John", "age": 30, "city": "New York"}
        self.wfile.write(json.dumps(data).encode())

    def handle_status(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

    def handle_404(self):
        self.send_response(404)
        self.end_headers()
        self.wfile.write(b"Endpoint not found")

if __name__ == "__main__":
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, SimpleHandler)
    print("Serving on http://localhost:8000")
    httpd.serve_forever()
