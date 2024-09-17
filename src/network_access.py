from secure_communication import create_secure_socket
from device_authentication import authenticate_device

def grant_network_access(device_id, token, secret_key, host, port):
    if authenticate_device(device_id, token, secret_key):
        secure_sock = create_secure_socket(host, port)
        print(f"Network access granted to {device_id}")
        secure_sock.close()
    else:
        print("Network access denied")

if __name__ == "__main__":
    device_id = 'device123'
    secret_key = 'supersecretkey'
    token = 'generated_token_here'  # Replace with the actual token
    host = 'example.com'
    port = 443
    grant_network_access(device_id, token, secret_key, host, port)
