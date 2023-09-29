import socket

serverAddressPort = ("127.0.0.1", 20001)  # destination
bufferSize = 1024  # message transmission size

# creates UDP server socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# sets up server to receive from clients
server.bind(serverAddressPort)
print("UDP server up and listening")
print("-------------------------------")


while (True):
    # recieves client message and client ip address
    msgFromClient, clientAddress = server.recvfrom(bufferSize)

    # prints client info
    print("Message from Client:{}".format(msgFromClient))
    print("Client IP Address: {}".format(clientAddress))

    # sends message back to client
    msgFromServer = "Hello UDP Client"
    bytesToSend = str.encode(msgFromServer)
    server.sendto(bytesToSend, clientAddress)
    print("----------------------------------")
    # kills the server
    if (msgFromClient.decode('utf-8') == "exit"):
        break
