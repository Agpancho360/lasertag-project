import socket

serverPort = 7501
clientPort = 7500
serverAddressPort = ("127.0.0.1", serverPort)  # broadcast
bufferSize = 1024  # message transmission size

# creates UDP client scoket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set socket options to enable broadcast
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

def sendMessage(msgFromClient):
    client.sendto(msgFromClient.encode('ascii'), (serverAddressPort))
    # client.sendto(msgFromClient.encode('ascii'), serverAddressPort) # sends message to the server

    # Recieves message from server
    data, serverAddress = client.recvfrom(bufferSize)
    msgFromServer = data.decode()
    print("Message from Server: {}".format(msgFromServer))

# while True:
# gets equipment code




# # kills the client
# if (msgFromClient == "exit"):
#     break
