from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

KEY = b'12345678901234567890123456789012'

def encrypt_file(data):
    iv = os.urandom(16)

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    cipher = Cipher(algorithms.AES(KEY), modes.CBC(iv))
    encryptor = cipher.encryptor()

    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    return iv + encrypted_data

def decrypt_file(encrypted_data):
    iv = encrypted_data[:16]
    actual_data = encrypted_data[16:]

    cipher = Cipher(algorithms.AES(KEY), modes.CBC(iv))
    decryptor = cipher.decryptor()

    padded_data = decryptor.update(actual_data) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()

    return data