from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        msg = f"Hello app Zmena V_8 Host={socket.gethostname()}\n Verze 8"
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(msg.encode())

HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
