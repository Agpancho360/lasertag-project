import socket

serverPort = 7501
clientPort = 7500
serverAddressPort = ("127.0.0.1", serverPort)  # broadcast
bufferSize = 1024  # message transmission size


def sendMessage(msgFromClient):
    # creates UDP client scoket
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Set socket options to enable broadcast
    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    client.sendto(msgFromClient.encode('ascii'), serverAddressPort)

    # client.sendto(msgFromClient.encode('ascii'), serverAddressPort) # sends message to the server

    # Recieves message from server
    data, serverAddress = client.recvfrom(bufferSize)
    msgFromServer = data.decode()
    print("Message from Server: {}".format(msgFromServer))
    client.close()

# while True:
# gets equipment code

# # kills the client
# if (msgFromClient == "exit"):
#     break

# Simulate sending different codes based on game events
# For example, sending code 53 to simulate the red base being scored
# and sending code 43 to simulate the green base being scored
# TRAFFIC GENERATOR WILL DO THIS
# send_message("53")
# send_message("43")