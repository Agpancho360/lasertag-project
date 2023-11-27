import socket
import dataBase 

serverPort = 7502
clientPort = 7500
serverAddressPort = ("127.0.0.1")  # destination
bufferSize = 1024  # message transmission size

# creates UDP server socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# sets up server to receive from clients
server.bind((serverAddressPort, serverPort))
print("UDP server up and listening")

greenPlayer = 0
redPlayer = 0

while (True):
    # recieves client message and client ip address
    msgFromClient, clientAddress = server.recvfrom(bufferSize)

    # prints client info
    print("Message from Client:{}".format(msgFromClient))
    print("Client IP Address: {}".format(clientAddress))
    print("----------------------------------")
    
    
    # Simulate game logic
    # For example, check for specific codes and take appropriate actions
    import playActionDisplay

    if msgFromClient.decode('utf-8') == "53":
        print("Code 53 received: Red base scored on!")
        randomGreenPlayer = dataBase.getRandomGreenPlayer()
        dataBase.updatePlayerScore(randomGreenPlayer, 100)
        if(dataBase.getPlayerName(randomGreenPlayer)[0] != "B" and dataBase.getPlayerName(randomGreenPlayer)[0] != " "):
            dataBase.updateEventString("Red base scored on by Player " + dataBase.getPlayerName(randomGreenPlayer))
            dataBase.updatePlayerName(randomGreenPlayer)
        # playActionDisplay.updateTableGreen(playActionDisplay.greenFrame)
        #update code to correctly select from someone that is red or green
        # Implement your scoring logic for the red team
    elif msgFromClient.decode('utf-8') == "43":
        print("Code 43 received: Green base scored on!")
        randomRedPlayer = dataBase.getRandomRedPlayer()
        dataBase.updatePlayerScore(randomRedPlayer, 100)
        if(dataBase.getPlayerName(randomRedPlayer)[0] != "B" and dataBase.getPlayerName(randomRedPlayer)[1] != " "):
            dataBase.updateEventString("Green base scored on by Player " + dataBase.getPlayerName(randomRedPlayer))
            dataBase.updatePlayerName(randomRedPlayer)
        # playActionDisplay.updateTableRed(playActionDisplay.redFrame)
        # Implement your scoring logic for the green team
    else:
        msgFromClientStr = msgFromClient.decode('utf-8')
        try:
            # Split the input string at the colon
            numbers = msgFromClientStr.split(":")

            # Extract the numbers
            player_1 = numbers[0]
            player_2 = numbers[1]

            #update Player score
            dataBase.updatePlayerScore(int(player_1), 10)
            dataBase.updateEventString("Player " + dataBase.getPlayerName(player_1) + " hit " + "Player " + dataBase.getPlayerName(player_2))
            
        except ValueError:
            print("That code is not recognized.")


        # sends message back to client
        msgFromServer = "Player " + msgFromClientStr + " has been confirmed: REPORTED"
        bytesToSend = str.encode(msgFromServer)
        server.sendto(bytesToSend, clientAddress)

# # kills the server
# if (msgFromClient.decode('utf-8') == "exit"):
#     break

