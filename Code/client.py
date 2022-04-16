from socket import *

serverName = "localhost" # 127.0.0.1
serverPort = 12300
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = "hello server"

clientSocket.sendto(message.encode(), (serverName, serverPort))
receivedMessage, serverAddress = clientSocket.recvfrom(2048)
print ("Received:", receivedMessage.decode())