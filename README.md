# Syntecxhub Encrypted File Transfer

## Project Overview

Syntecxhub Encrypted File Transfer is a cybersecurity-focused Python project that demonstrates secure file transmission using AES encryption, HMAC integrity verification, and client-server socket communication.

The project simulates a secure file transfer environment where files are:
- encrypted before transmission
- securely transferred over a network socket
- verified for integrity using HMAC-SHA256
- decrypted and stored securely on the receiving server

This project was built to strengthen practical cybersecurity, networking, and secure programming skills.

---

# Features

## Secure File Encryption
- AES-256 encryption using Python cryptography library
- CBC mode encryption with randomly generated IVs

## Integrity Verification
- HMAC-SHA256 integrity validation
- Detects unauthorized file modification or tampering

## Secure Client-Server Communication
- TCP socket-based communication
- Secure encrypted file transfer workflow

## Secure File Storage
- Files are decrypted and securely stored on the server side

---

# Technologies Used

- Python 3
- Socket Programming
- AES Encryption
- HMAC-SHA256
- Cryptography Library
- TCP/IP Networking

---

# Project Structure

```text
Syntecxhub_Encrypted_File_Transfer
│
├── client
│   └── client.py
│
├── server
│   └── server.py
│
├── encryption
│   ├── aes_utils.py
│   └── hmac_utils.py
│
├── received_files
│
├── screenshots
│
├── testfile.txt
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore

How It Works
Step 1 — Client Reads File

The client application reads the selected file from disk.

Step 2 — AES Encryption

The file contents are encrypted using AES encryption before transmission.

Step 3 — HMAC Generation

An HMAC-SHA256 hash is generated to ensure file integrity.

Step 4 — Secure File Transfer

The encrypted file and HMAC are transmitted securely to the server using TCP sockets.

Step 5 — Integrity Verification

The server verifies the HMAC to ensure the file was not modified during transmission.

Step 6 — File Decryption

If integrity validation succeeds, the file is decrypted.

Step 7 — Secure Storage

The decrypted file is stored inside the received_files directory.

Installation
Clone Repository
git clone https://github.com/musechuene-commits/Syntecxhub_Encrypted_File_Transfer.git
Navigate Into Project
cd Syntecxhub_Encrypted_File_Transfer
Install Requirements
pip install -r requirements.txt
Usage
Start Server
python server/server.py
Start Client

Open a second terminal:

python client/client.py

When prompted:

Enter file path to send:

Example:

testfile.txt
Example Output
Client
FILE_RECEIVED_SUCCESSFULLY
Server
[SUCCESS] File received and verified: testfile.txt
Screenshots
Secure File Transfer

(Add screenshot here)

Server Verification

(Add screenshot here)

Received Files

(Add screenshot here)

Security Concepts Demonstrated
AES Encryption
HMAC Integrity Validation
Secure File Transmission
TCP Socket Programming
Secure Storage Concepts
Cryptography Fundamentals
Client-Server Security Architecture
Skills Demonstrated
Cybersecurity Skills
Encryption implementation
Integrity verification
Secure communication
Secure file handling
Defensive programming
Technical Skills
Python programming
Socket programming
Networking fundamentals
File handling
Troubleshooting
Future Improvements
TLS/SSL encryption
Multi-client support
File size validation
Secure authentication system
Logging and monitoring
GUI interface
Secure key management
Disclaimer

This project was created strictly for educational and portfolio purposes in a controlled local environment.

Author
Musa Chuene
LinkedIn: https://linkedin.com/in/musa-chuene-57a4461a8
GitHub: https://github.com/musechuene-commits