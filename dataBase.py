import os
from supabase import create_client
# import udp_client
import socket
import random


# setupt to get into the project database
SUPABASE_URL = 'https://qjqnfmauqqdjpppdlrdq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFqcW5mbWF1cXFkanBwcGRscmRxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5Mzk0MjMzNSwiZXhwIjoyMDA5NTE4MzM1fQ.C9GRRux8dixBbjh_nEHhyZotMqhXSn6OY0BEbmcGyik'
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

clientAddressPort   = ("127.0.0.1", 7500)
UDPClientSocketTransmit = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


class Player:
    def __init__(self, first_name, last_name, codename, team):

        response = supabase.table('Player').select(
            'ID', count='exact').execute()
        player_ID = response.count + 1
        response = supabase.table('Player').select(
            'equipment_ID', count='exact').execute()
        equip_ID = response.count + 100
        self.ID = player_ID
        self.first_name = first_name
        self.last_name = last_name
        self.codename = codename
        self.team = team
        self.equipment_ID = equip_ID

    def insertPlayer(self):

        data = {'ID': self.ID,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'codename': self.codename,
                'team': self.team,
                'equipment_ID': self.equipment_ID}
        supabase.table('Player').insert(data).execute()
        msg = str(self.equipment_ID)
        UDPClientSocketTransmit.sendto(str.encode(str(msg)), clientAddressPort)
        # udp_client.sendMessage(msgFromClient)

def getRandomGreenPlayer():
    response = supabase.table('Player').select('*').eq('team', 'Green').execute()
    result = response.data
    length = len(result)
    random_number = result[random.randint(1, length-1)]['ID']
    return random_number

def getRandomRedPlayer():
    response = supabase.table('Player').select('*').eq('team', 'Red').execute()
    result = response.data
    length = len(result)
    random_number = result[random.randint(1, length-1)]['ID']
    return random_number

def updatePlayerScore(id, pointsToAdd):
    response = supabase.table('Player').select('player_score').eq('ID', id).execute()
    score = response.data
    player_score = score[0]['player_score']
    supabase.table('Player').update({'player_score' : str((int(player_score) + pointsToAdd))}).eq('ID', id).execute()

def getMinimumIDRED():
    response = supabase.from_('Player').select('ID').eq('team', 'Red').order('ID').limit(1).execute()
    min = response.data
    min_id = min[0]['ID']
    return min_id

def getMinimumIDGreen():
    response = supabase.from_('Player').select('ID').eq('team', 'Green').order('ID').limit(1).execute()
    min = response.data
    min_id = min[0]['ID']
    return min_id

def getRedTeamScore():
    data, count = supabase.table('Player').select('player_score').eq('team', 'Red').execute()
    red_team_score = sum(entry['player_score'] for entry in data[1])
    return red_team_score

def getGreenTeamScore():
    data, count = supabase.table('Player').select('player_score').eq('team', 'Green').execute()
    green_team_score = sum(entry['player_score'] for entry in data[1])
    return green_team_score

def getRedTeamCount():
    data, count = supabase.table('Player').select('*', count='exact').eq('team', 'Red').execute()
    return len(data[1])

def getGreenTeamCount():
    data, count = supabase.table('Player').select('*', count='exact').eq('team', 'Green').execute()
    return len(data[1])

def getRedTeamData():
    data, count = supabase.table('Player').select(
        'ID, first_name, last_name, codename').eq('team', 'Red').execute()
    return data[1]

def getGreenTeamData():
    data, count = supabase.table('Player').select(
        'ID, first_name, last_name, codename').eq('team', 'Green').execute()
    return data[1]

def getRedPlayerData():
    data, count = supabase.table('Player').select(
        'codename, player_score').eq('team', 'Red').execute()
    return data[1]

def getGreenPlayerData():
    data, count = supabase.table('Player').select(
        'codename, player_score').eq('team', 'Green').execute()
    return data[1]

def clearData():
    supabase.table('Player').delete().gte('ID', 1).execute()



# example of data that could be input into the 'Player' table
# data = [
#     {
#         'ID': 1,  # primary key and must be unique
#         'first_name': 'Kaden',
#         'last_name': 'Ramirez',
#         'codename': 'Eagleye',  # must be unique
#         'team': 'Red',  # must be Red or Green (case sensitive)
#         'equipment_ID': 100  # must be unique
#     },
#     {
#         'ID': 2,  # primary key and must be unique
#         'first_name': 'Alex',
#         'last_name': 'Guzman',
#         'codename': 'Thunder_Lips',  # must be unique
#         'team': 'Green',  # must be Red or Green (case sensitive)
#         'equipment_ID': 101  # must be unique
#     },
# ]

# player = Player('Alex', 'Tavaraz', 'Uknown', 'Green') # creates player with these attributes
# player.insertPlayer() # inserts the created player into the Player table in the database

# prints all the data in the 'Player' table
# print(supabase.table('Player').select('*').execute().data)

# inserts data into the player table
# supabase.table('Player').insert(data).execute()

# deletes data where 'ID' is equal to 3
# supabase.table('Player').delete().eq('ID', 3).execute()

# updates the Player table entry codename that has 'ID' = 2 to 'FunnyName'
# supabase.table('Player').update({'codename' : 'FunnyName'}).eq('ID', 2).execute()
