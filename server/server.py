import socket
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from encryption.aes_utils import decrypt_file
from encryption.hmac_utils import verify_hmac

HOST = "127.0.0.1"
PORT = 5000
SAVE_FOLDER = "received_files"

os.makedirs(SAVE_FOLDER, exist_ok=True)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"[SERVER STARTED] Listening on {HOST}:{PORT}")

while True:
    conn, addr = server.accept()
    print(f"[CONNECTED] {addr}")

    filename = conn.recv(1024).decode()
    conn.send(b"FILENAME_RECEIVED")

    received_hmac = conn.recv(1024).decode()
    conn.send(b"HMAC_RECEIVED")

    encrypted_data = conn.recv(10000000)

    if verify_hmac(encrypted_data, received_hmac):
        decrypted_data = decrypt_file(encrypted_data)

        file_path = os.path.join(SAVE_FOLDER, filename)

        with open(file_path, "wb") as file:
            file.write(decrypted_data)

        print(f"[SUCCESS] File received and verified: {filename}")
        conn.send(b"FILE_RECEIVED_SUCCESSFULLY")
    else:
        print("[ERROR] HMAC verification failed.")
        conn.send(b"FILE_INTEGRITY_FAILED")

    conn.close()