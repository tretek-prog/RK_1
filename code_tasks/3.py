import json
import random
import requests
from http.server import BaseHTTPRequestHandler
from helpers import http_server
from domonic import *

# urllib3 for url parse


class BookHandler(BaseHTTPRequestHandler):
    # Handler for the GET random number info
    def do_GET(self):
        print('Get request received')
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        r = random.randint(0, 100)
        resp = requests.get(f"http://numbersapi.com/{r}")
        respon = render(
            html(
                head(
                ),
                body(
                    style(
                        'BODY {background: url(https://capital2020.ru/d/mgtu_im_n_e_baumana_moskva.jpg) no-repeat;}',
                        _type="text/css",
                        ),
                    header(b('Random interesting fact about ', r,
                    _style =
                    '''font-size: 30px;
                    color: green;
                    ''')),
                    p(resp.content.decode())
                )
            )
        )
        self.wfile.write(respon.encode())



if __name__ == "__main__":
    server = http_server.Server(handler=BookHandler)
    server.run()
