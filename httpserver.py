#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import threading
x = None
httpd = None

class StoppableHTTPServer(ThreadingMixIn, HTTPServer):
    """An Http Server we can stop programmatically"""
    def run(self):
        try:
            self.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            # Clean-up server (close socket, etc.)
            self.server_close()

class S(BaseHTTPRequestHandler):
    """Default implementation class echoing the sent requests"""
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        print("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))
    def log_message(self, format, *args):
        print(f"{format}/{args}")        

def up(server_class=StoppableHTTPServer, handler_class=S, port=8080, output=None):
    """Actual server start"""
    global httpd
    server_address = ('127.0.0.1', port)
    handler_class.extensions_map={
        '.manifest': 'text/cache-manifest',
        '.html': 'text/html',
        '.png': 'image/png',
        '.jpg': 'image/jpg',
        '.svg': 'image/svg+xml',
        '.css': 'text/css',
        '.js': 'application/x-javascript',
        '.json': 'application/json',
        '.xml': 'application/xml' ,      
        '': 'application/octet-stream', # Default
        }    
    httpd = server_class(server_address, handler_class)
    httpd.output = output
    print('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print('Stopping httpd...\n')
    
def start(server_class=StoppableHTTPServer,handler_class=S,port=8080,output=None):
    """Ask for server start"""
    global x
    # print("Main    : before creating thread")
    x = threading.Thread(target=up, args=(), kwargs={'server_class': server_class, 'handler_class': handler_class, 'port': port, 'output': output})
    # print("Main    : before running thread")
    x.start()

def stop():
    """Ask for server stop"""
    global httpd
    if httpd is not None:
        httpd.shutdown()
        httpd.server_close()
        httpd = None

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        start(port=int(argv[1]))
    else:
        start()