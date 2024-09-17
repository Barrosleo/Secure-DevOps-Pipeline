import hashlib
import hmac

def generate_device_token(device_id, secret_key):
    return hmac.new(secret_key.encode(), device_id.encode(), hashlib.sha256).hexdigest()

def authenticate_device(device_id, token, secret_key):
    expected_token = generate_device_token(device_id, secret_key)
    return hmac.compare_digest(expected_token, token)

if __name__ == "__main__":
    device_id = 'device123'
    secret_key = 'supersecretkey'
    token = generate_device_token(device_id, secret_key)
    print(f"Generated token: {token}")
    is_authenticated = authenticate_device(device_id, token, secret_key)
    print(f"Device authenticated: {is_authenticated}")
