import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("",PORT),Handler) as http:
    print("server running on port",PORT)
    http.serve_forever()