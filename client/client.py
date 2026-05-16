import socket
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from encryption.aes_utils import encrypt_file
from encryption.hmac_utils import generate_hmac

HOST = "127.0.0.1"
PORT = 5000

def send_file(file_path):

    filename = os.path.basename(file_path)

    with open(file_path, "rb") as file:
        file_data = file.read()

    encrypted_data = encrypt_file(file_data)

    file_hmac = generate_hmac(encrypted_data)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((HOST, PORT))

    client.send(filename.encode())

    client.recv(1024)

    client.send(file_hmac.encode())

    client.recv(1024)

    client.send(encrypted_data)

    response = client.recv(1024).decode()

    print(response)

    client.close()

if __name__ == "__main__":

    path = input("Enter file path to send: ")

    send_file(path)