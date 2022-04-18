from socket import * # include socket lib
import time
import json
import sys

class Client:
    socket = 0
    start = 0

    #constructor
    def __init__(self, address, port):
        self.address = address
        self.port = port

    # create socket
    def Create(self):
        self.socket = socket(AF_INET, SOCK_DGRAM)
        self.socket.settimeout(1) # set timeout on blocking socket operations

    # send message into socket
    def Send(self, message):
        self.start = time.time() # system time before send
        self.socket.sendto(message.encode(), (self.address, self.port))

    # read message froms rocket
    def Receive(self):
        receivedMessage,serverAddress = self.socket.recvfrom(2048)
        end = time.time() # system time after response
        print("Server:", receivedMessage.decode())
        print("RTT:", round(((end - self.start)* 1000), 3), "ms\n")

exist = False

serverAddress = "127.0.0.1"
serverPort = 12300

# simple ping pong
client = Client(serverAddress, serverPort) # create client object
client.Create()
client.Send("Hello Server")
try:
    client.Receive()
except timeout as e: # handle timeout 
        print("No reply received within one second. Error:", e)
        sys.exit(1) # exit program

# read/send json file data
message = input("Date: ") # user input requested date
with open("../wheel_rotation_sensor_data.json", "r") as file: # open json file
    text = file.read() # read json file and adjust to right format
    text = text.replace('\'','\"')
    data = json.loads(text) # deserialize to python obj

    for i in data: # iterate over json data
        if i["date"] == message: # if date exists in file
            exist = True
            item = json.dumps(i, indent = 5) # serialize to json formatted string
            client.Send(item)

# receive response
if exist == False:
    print("\nNo data found for this date")
else: 
    exist = False
    try:
        client.Receive()
    except timeout as e:
        print("No reply received within one second. Error:", e)