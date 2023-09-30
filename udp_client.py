import socket

serverAddressPort = ("127.0.0.1", 20001)  # destination
bufferSize = 1024  # message transmission size

# creates UDP client scoket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def sendMessage(msgFromClient):
    client.sendto(msgFromClient.encode('ascii'), serverAddressPort) # sends message to the server

    # Recieves message from server
    msgFromServer = client.recvfrom(bufferSize)
    print("Message from Server{}:  ".format(msgFromServer[0]))

# while True:
# gets equipment code




# # kills the client
# if (msgFromClient == "exit"):
#     break
