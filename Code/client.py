from socket import * # include socket lib
import time
import json

exist = False

address = "127.0.0.1"
port = 12300

# create client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

# sending data
message = "Hello server"
start = time.time() # system time before send
clientSocket.sendto(message.encode(), (address, port))

# receiving data
receivedMessage, serverAddress = clientSocket.recvfrom(2048)
end = time.time() # system time after response
print("Server:", receivedMessage.decode())
print("RTT:", round(((end - start)* 1000), 3), "ms\n")


message = input("Date: ")
with open("../wheel_rotation_sensor_data.json", "r") as file:
    text = file.read()
    text = text.replace('\'','\"')
    text = text.replace('None','"None"')
    data = json.loads(text)

    for i in data:
        if i["date"] == message:
            exist = True
            item = json.dumps(i, indent = 5)
            start = time.time()
            clientSocket.sendto(item.encode(), (address, port))

if exist == False:
    print("\nNo data found for this date")
else: 
    exist = False
    try:
        receivedMessage, serverAddress = clientSocket.recvfrom(2048)
        receivedMessage, serverAddress = clientSocket.recvfrom(2048)
        end = time.time()
        print("\nServer:", receivedMessage.decode())
        print("RTT:", round(((end - start)* 1000), 3), "ms")
    except timeout as e:
        print("No reply received within one second. Error:", e)
