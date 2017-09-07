from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from deploymentsample import DeploymentSample

ADDR = "0.0.0.0"
PORT = 8000

class RequestHandler(BaseHTTPRequestHandler):        
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        content = self.rfile.read(content_length)
        message = "Hello deployed code from "
        message = DeploymentSample(message).getHelloFromHost()

        message = message + ": " + content + "\n"
        self.send_response(200)
        self.send_header('Content-Length', len(str(message)))
        self.end_headers()
        self.wfile.write(message)
        return

httpd = HTTPServer((ADDR, PORT), RequestHandler)
httpd.serve_forever()
