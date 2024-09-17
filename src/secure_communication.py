import ssl
import socket

def create_secure_socket(host, port):
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    secure_sock = context.wrap_socket(sock, server_hostname=host)
    secure_sock.connect((host, port))
    return secure_sock

if __name__ == "__main__":
    host = 'example.com'
    port = 443
    secure_sock = create_secure_socket(host, port)
    print(f"Secure connection established with {host}:{port}")
    secure_sock.close()
