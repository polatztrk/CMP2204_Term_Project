import socket
import json

# Define UDP listening address and port
UDP_IP = ''  # Listen on all available interfaces
UDP_PORT = 5001

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind socket to listening address and port
sock.bind((UDP_IP, UDP_PORT))
print("Server is Ready")
# Listen for incoming UDP messages
my_dict={}
while True:
    data, addr = sock.recvfrom(8096)
    json_data = json.loads(data.decode())

    for i in json_data['chunks']:
        if i in my_dict:
            if addr[0] in my_dict[i]:
                continue
            else:
                my_dict[i].append(addr[0])
        else:
            my_dict[i] = [addr[0]]
        with open('my_dict.json', 'w') as file:
            json.dump(my_dict, file)

    print("my_dict saved as my_dict.json")
    print(my_dict)






# Close socket
sock.close()