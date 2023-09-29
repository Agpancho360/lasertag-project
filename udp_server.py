import socket
localIP = "127.0.0.1" #local host
localPort = 20001 #may need to be changed after
bufferSize = 1024

msgFromServer = "Hello UDP Client"
bytesToSend = str.encode(msgFromServer)

#creates UDP server socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((localIP, localPort))
print("UDP server up and listening")
while (True):
    bytesAddressPair = server.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP Address: {}".format(address)

    print(clientMsg)
    print(clientIP)
    server.sendto(bytesToSend, address)
