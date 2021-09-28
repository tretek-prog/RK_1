import json
import random
import requests

from http.server import BaseHTTPRequestHandler
from helpers import http_server

# urllib3 for url parse


class BookHandler(BaseHTTPRequestHandler):
    # Handler for the GET random number info
    def do_GET(self):
        print('Get request received')
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        resp = requests.get(f"http://numbersapi.com/{random.randint(0, 100)}")
        self.wfile.write(json.dumps({'status': resp.status_code, 'content': resp.content.decode()}).encode())


if __name__ == "__main__":
    server = http_server.Server(handler=BookHandler)
    server.run()