from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

httpd = HTTPServer(("0.0.0.0", 8443), SimpleHTTPRequestHandler)

sslctx = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
sslctx.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

httpd.socket = sslctx.wrap_socket(
    httpd.socket,
    server_side=True
)

print("HTTPS running on 8443")
httpd.serve_forever()
