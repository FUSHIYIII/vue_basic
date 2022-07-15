#coding=UTF-8
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from time import sleep

host = ('localhost', 80)
filepath = './filepath/vue.js'

with open(filepath, 'r') as f:
    buf = f.read()

class Resquest(BaseHTTPRequestHandler):
    timeout = 5
    server_version = "Apache"
    def do_GET(self):
        path = self.path
        if path == '/resource/0s/vue.js':
            sleep(0)
            self.send_response(200)
            self.send_header("Content-type",'application/json')
            self.end_headers()
            self.wfile.write(buf.encode())

        elif path == '/resource/2s/vue.js':
            sleep(2)
            self.send_response(200)
            self.send_header("Content-type",'application/json')
            self.end_headers()
            self.wfile.write(buf.encode())

        elif path == '/resource/5s/vue.js':
            sleep(5)
            self.send_response(200)
            self.send_header("Content-type",'application/json') 
            self.end_headers()
            self.wfile.write(buf.encode())
        
        else:
            self.send_response(200)
            self.send_header("Content-type","text/html") 
            self.end_headers()
            notfoundpage = "<h1>RESOURCE FOUND</h1>"
            self.wfile.write(notfoundpage.encode())
 
if __name__ == '__main__':
    server = HTTPServer(host, Resquest)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()