import http.server
from prometheus_client import start_http_server
from prometheus_client import Counter

REQUESTS=Counter('hello_worlds_total', 'hellow worlds requested.')

EXCEPTIONS=Counter("hello_world_exceptions_total", 'exceptions serving hello world.')

class MyHandler(http.server.BaseHTTPRequestHandler):
    @EXCEPTIONS.count_exceptions()
    def do_GET(self):
        REQUESTS.inc()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"hello world")

if __name__ == "__main__":
    start_http_server(8000)
    server = http.server.HTTPServer(('localhost', 8001), MyHandler)
    server.serve_forever()