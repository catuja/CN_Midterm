from socket import * # include socket lib
import time
import json

address = "127.0.0.1"
port = 12300

# create client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# sending data
message = "Hello server"
start = time.time() # system time before send
clientSocket.sendto(message.encode(), (address, port))

# receiving data
receivedMessage, serverAddress = clientSocket.recvfrom(2048)
end = time.time() # system time after response
print("Server:", receivedMessage.decode())
print("RTT:", round(((end - start)* 1000), 3), "ms")


message = input("Date: ")
with open("../wheel_rotation_sensor_data.json", "r") as file:
    text = file.read()
    text = text.replace('\'','\"')
    text = text.replace('None','"None"')
    data = json.loads(text)

    for i in data:
        if i["date"] == message:
            #print("g")
            item = json.dumps(i, indent = 5)
            start = time.time()
            clientSocket.sendto(item.encode(), (address, port))

receivedMessage, serverAddress = clientSocket.recvfrom(2048)
end = time.time()
print("Server:", receivedMessage.decode())
print("RTT:", round(((end - start)* 1000), 3), "ms")
