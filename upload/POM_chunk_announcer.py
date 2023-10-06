
import os
import math
import json
import socket
import time

UDP_IP = '192.168.1.255'  # Broadcast address
UDP_PORT = 5001

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)


folder_path="chunks"
filename = input("Please Enter the File Name with Lowercase Letter and With It's extension: ")
content_name, extension = filename.split('.')
c = os.path.getsize("data/"+filename)

print("Total Size is: ",c)
CHUNK_SIZE = math.ceil(math.ceil(c)/5)
print("Every Chunks Size are: ",CHUNK_SIZE)
print("Total Number of Chunk is: 5")

index = 1
with open("data/"+filename, 'rb') as infile:

    chunk = infile.read(int(CHUNK_SIZE))
    while chunk:

        chunkname = content_name+'_'+str(index)
        print(f"chunk {index} name is: " + chunkname + "\n")
        with open("chunks/"+chunkname,'wb+') as chunk_file:
            chunk_file.write(chunk)
            index += 1
            chunk = infile.read(int(CHUNK_SIZE))
chunk_file.close()

print("Starting to Announce...")

file_names = os.listdir(folder_path)

data = {'chunks': file_names}
json_data = json.dumps(data)

with open('chunks.json', 'w') as f:
    f.write(json_data)
while True:
    sock.sendto(json_data.encode(), (UDP_IP, UDP_PORT))
    time.sleep(5)

sock.close()
