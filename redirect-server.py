from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs


class MainHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.handleRequest()

    def do_POST(self):
        self.handleRequest()

    def handleRequest(self):
        parsed_url = urlparse(self.path)
        query_params = parse_qs(parsed_url.query)
        if "l" in query_params:
            redirect_url = query_params["l"][0]
            self.send_response(303)
            self.send_header('Location', redirect_url)
            self.end_headers()
        else:
            self.send_error(400, "error")


if __name__ == "__main__":
    httpd = HTTPServer(("0.0.0.0", 8150), MainHTTPRequestHandler)
    httpd.serve_forever()
