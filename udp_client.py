import socket

serverAddressPort = ("127.0.0.1", 20001)  # destination
bufferSize = 1024  # message transmission size

# creates UDP client scoket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# while True:
# gets equipment code
msgFromClient = "Player 1 has been hit "

# Sending message to server
client.sendto(msgFromClient.encode('ascii'), serverAddressPort)

# Recieves message from server
msgFromServer = client.recvfrom(bufferSize)
print("Message from Server{}:  ".format(msgFromServer[0]))

# # kills the client
# if (msgFromClient == "exit"):
#     break
