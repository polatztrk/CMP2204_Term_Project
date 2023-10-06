import json
import socket
from datetime import datetime


def downloader():
    # Read the JSON file
    with open('my_dict.json', 'r') as file:
        my_dict = json.load(file)

    # Chunk Downloader configuration
    CHUNK_COUNT = 5
    DOWNLOAD_LOG_FILE = 'download_log.txt'

    # Prompt the user to specify the content to download
    filename = input("Enter the content name to download with it's file extension: ")
    content_name, extension = filename.split('.')
    chunknames = [content_name + '_1', content_name + '_2', content_name + '_3', content_name + '_4',
                  content_name + '_5']

    for chunk_number in range(1, CHUNK_COUNT + 1):
        chunk_name = f"{content_name}_{chunk_number}"
        for ip_address in my_dict[chunk_name]:
            try:
                # Server address and port
                SERVER_IP = ip_address
                SERVER_PORT = 5000

                # Create a TCP socket
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                # Connect to the server
                sock.connect((SERVER_IP, SERVER_PORT))
                # Create a JSON payload with the requested content
                payload = {"requested content": chunk_name}
                with open('req.json', 'w') as file:
                    json.dump(payload, file)
                payload_str = json.dumps(payload)

                # Send the payload to the server
                sock.send(payload_str.encode())

                # Receive the chunk data from the server and save it
                file_name = f"{chunk_name}"
                with open("chunks/" + file_name, 'wb') as file:
                    while True:
                        chunk_data = sock.recv(4096)  # Adjust the buffer size as needed
                        if not chunk_data:
                            break
                        file.write(chunk_data)
                file.close()
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_entry = f"{timestamp}: {chunk_name} downloaded from {ip_address}\n"
                with open(DOWNLOAD_LOG_FILE, 'a') as log_file:
                    log_file.write(log_entry)

                break  # Exit the loop if download is successful
            except:
                continue  # Try downloading from the next IP address if an error occurs

        else:
            # Display a warning message if the chunk cannot be downloaded from any IP address
            print(f"CHUNK {chunk_name} CANNOT BE DOWNLOADED FROM ONLINE PEERS.")

    # Close the TCP session
    sock.close()

    with open("data/" + filename, 'wb') as outfile:
        for chunk in chunknames:
            with open("chunks/" + chunk, 'rb') as infile:
                outfile.write(infile.read())
            infile.close()
    # Inform the user that the file has been successfully downloaded
    print("File has been successfully downloaded.")

# Persist the service without terminating
while True:
    downloader()
    continue




