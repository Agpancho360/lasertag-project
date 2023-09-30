import socket

serverPort = 7501
clientPort = 7500
serverAddressPort = ("127.0.0.1")  # destination
bufferSize = 1024  # message transmission size

# creates UDP server socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# sets up server to receive from clients
server.bind((serverAddressPort, serverPort))
print("UDP server up and listening")


# while (True):
# recieves client message and client ip address
msgFromClient, clientAddress = server.recvfrom(bufferSize)

# prints client info
print("Message from Client:{}".format(msgFromClient))
print("Client IP Address: {}".format(clientAddress))
print("----------------------------------")

# sends message back to client
msgFromClientStr = msgFromClient.decode('utf-8')
msgFromServer = "Player " + msgFromClientStr + " has been confirmed: REPORTED"
bytesToSend = str.encode(msgFromServer)
server.sendto(bytesToSend, clientAddress)

# # kills the server
# if (msgFromClient.decode('utf-8') == "exit"):
#     break
