from socket import * # include socket lib

address = "127.0.0.1"
port = 12300

# create and bind server socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((address, port))

message = "Received"

print ("The server is ready to receive")

while True:

    # receiving data
    receivedMessage, clientAddress = serverSocket.recvfrom(2048)
    print ("Client:", receivedMessage.decode())

    # sending data
    serverSocket.sendto(message.encode(), clientAddress)
