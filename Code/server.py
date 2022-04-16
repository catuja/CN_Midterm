from mailbox import Message
from socket import *

serverName = "localhost" # 127.0.0.1
serverPort = 12300
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverName, serverPort))

message = "hello client"

print ("The server is ready to receive")

while True:
    receivedMessage, clientAddress = serverSocket.recvfrom(2048)
    print ("Received:", receivedMessage.decode())
    serverSocket.sendto(message.encode(), clientAddress)
