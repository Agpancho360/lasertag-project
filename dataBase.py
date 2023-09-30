import os
from supabase import create_client

# setupt to get into the project database
SUPABASE_URL = 'https://qjqnfmauqqdjpppdlrdq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFqcW5mbWF1cXFkanBwcGRscmRxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5Mzk0MjMzNSwiZXhwIjoyMDA5NTE4MzM1fQ.C9GRRux8dixBbjh_nEHhyZotMqhXSn6OY0BEbmcGyik'
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

class Player:
    def __init__(self, first_name, last_name, codename, team):
        
        response = supabase.table('Player').select('ID', count='exact').execute()
        player_ID = response.count + 1
        response = supabase.table('Player').select('equipment_ID', count='exact').execute()
        equip_ID = response.count + 100
        self.ID = player_ID
        self.first_name = first_name
        self.last_name = last_name
        self.codename = codename
        self.team = team
        self.equipment_ID = equip_ID
    
    def insertPlayer(self):
        
        data = {'ID' : self.ID,
                'first_name': self.first_name,
                'last_name': self.last_name,
                'codename': self.codename,
                'team' : self.team,
                'equipment_ID' : self.equipment_ID}
        supabase.table('Player').insert(data).execute()


# example of data that could be input into the 'Player' table
data = [
    {
        'ID': 1,  # primary key and must be unique
        'first_name': 'Kaden',
        'last_name': 'Ramirez',
        'codename': 'Eagleye',  # must be unique
        'team' : 'Red', # must be Red or Blue (case sensitive)
        'equipment_ID' : 100 # must be unique
    },
    {
        'ID': 2,  # primary key and must be unique
        'first_name': 'Alex',
        'last_name': 'Guzman',
        'codename': 'Thunder_Lips',  # must be unique
        'team' : 'Blue', # must be Red or Blue (case sensitive)
        'equipment_ID' : 101 # must be unique
    },
]

# player = Player('Alex', 'Tavaraz', 'Uknown', 'Blue') # creates player with these attributes
# player.insertPlayer() # inserts the created player into the Player table in the database

# prints all the data in the 'Player' table
# print(supabase.table('Player').select('*').execute().data)

# inserts data into the player table
#supabase.table('Player').insert(data).execute()

# deletes data where 'ID' is equal to 3
# supabase.table('Player').delete().eq('ID', 3).execute()

# updates the Player table entry codename that has 'ID' = 2 to 'FunnyName'
# supabase.table('Player').update({'codename' : 'FunnyName'}).eq('ID', 2).execute()
