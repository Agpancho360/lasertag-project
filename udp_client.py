import socket

msgFromClient = "This message is from Client"
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

#creates UDP client scoket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(bytesToSend, serverAddressPort)

msgFromServer = client.recvfrom(bufferSize)
msg = "Message from Server{}".format(msgFromServer[0])
print(msg)
