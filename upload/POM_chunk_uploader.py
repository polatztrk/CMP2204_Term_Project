
import socket
import json
import os
from datetime import datetime

# Chunk Uploader configuration
UPLOAD_LOG_FILE = 'upload_log.txt'

# Server address and port
SERVER_IP = '192.168.1.41'
SERVER_PORT = 5000

# Create a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address and port
sock.bind((SERVER_IP, SERVER_PORT))

# Listen for incoming connections
sock.listen()

# Print a message indicating that the Chunk Uploader is ready
print("Chunk Uploader is ready and listening for connections.")

# Function to handle incoming connections
def handle_connection(conn):
    # Receive the payload from the client
    payload_str = conn.recv(1024).decode()

    # Parse the JSON payload
    payload = json.loads(payload_str)
    requested_chunk = payload.get('requested content')

    # Check if the requested chunk exists
    if os.path.exists("chunks/"+requested_chunk):
        # Open the file and read its contents
        with open("chunks/"+requested_chunk, 'rb') as file:
            while True:
                chunk_data = file.read(4096)
                if not chunk_data:
                    break
                conn.send(chunk_data)

        # Log the upload entry
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{requested_chunk}: {timestamp}, sent to {conn.getpeername()[0]}\n"
        with open(UPLOAD_LOG_FILE, 'a') as log_file:
            log_file.write(log_entry)

    # Close the connection
    conn.close()

# Accept incoming connections and handle them
while True:
    conn, addr = sock.accept()
    print(f"New connection from {addr[0]}:{addr[1]}")
    handle_connection(conn)

# Persist the service without terminating
while True:
    continue