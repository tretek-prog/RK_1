#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./http_server.py [<port>]
"""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer, CGIHTTPRequestHandler

PORT_NUMBER = 8080


class MyHandler(BaseHTTPRequestHandler):
    # Handler for the GET requests
    def do_GET(self):
        print('Get request received')
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'status': 200, 'content': 'Hello world!'}).encode())

    # Handler for the POST requests
    def do_POST(self):
        print('Get post received')
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        self.wfile.write(post_body)


class Server:
    def __init__(self, handler=MyHandler):
        # Create a web server and define the handler to manage the
        # incoming request
        # self.server = HTTPServer(('', PORT_NUMBER), CGIHTTPRequestHandler)
        self.server = HTTPServer(('', PORT_NUMBER), handler)

    def run(self, port=PORT_NUMBER):
        try:
            print('Started httpserver on port ', port)
            # Wait forever for incoming http requests
            self.server.serve_forever()

        except KeyboardInterrupt:
            print('Shutting down the web server')
            self.server.socket.close()


if __name__ == '__main__':
    from sys import argv

    server = Server()
    if len(argv) == 2:
        server.run(port=int(argv[1]))
    else:
        server.run()
