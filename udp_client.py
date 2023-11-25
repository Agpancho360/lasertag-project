import socket

serverPort = 7501
clientPort = 7500
serverAddressPort = ("127.0.0.1", serverPort)  # original server
bufferSize = 1024  # message transmission size

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# print("THIS IS IT:" + str(socket.SO_BROADCAST))

# Bind the client to a specific address and port for receiving messages
client.bind(("127.0.0.1", clientPort))
print("Client Up and listening")

def forwardMessage(msgFromClient, targetServerAddress):
    # creates UDP client socket
    client.sendto(msgFromClient.encode('ascii'), targetServerAddress)

    # Receive message from server
    # data, serverAddress = client.recvfrom(bufferSize)
    # msgFromServer = data.decode()
    # print("Message from Server: {}".format(msgFromServer))

while True:
    # Receive message from a different server
    data, serverAddress = client.recvfrom(bufferSize)
    msgFromOtherServer = data.decode()
    print("Message from Server: {}".format(msgFromOtherServer))
    # forwardMessage(msgFromOtherServer, serverAddressPort)

    # You can add more logic here based on the received message if needed


    # You can add more logic here based on the received message if needed

# Simulate sending different codes based on game events
# For example, sending code 53 to simulate the red base being scored
# and sending code 43 to simulate the green base being scored
# TRAFFIC GENERATOR WILL DO THIS
# send_message("53")
# send_message("43")
