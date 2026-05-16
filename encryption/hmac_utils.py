import hmac
import hashlib

SECRET_KEY = b"supersecretkey"

def generate_hmac(data):
    return hmac.new(SECRET_KEY, data, hashlib.sha256).hexdigest()

def verify_hmac(data, received_hmac):
    calculated_hmac = generate_hmac(data)
    return hmac.compare_digest(calculated_hmac, received_hmac)