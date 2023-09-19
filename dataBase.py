import os
from supabase import create_client

#setupt to get into the project database
SUPABASE_URL = 'https://qjqnfmauqqdjpppdlrdq.supabase.co'
SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFqcW5mbWF1cXFkanBwcGRscmRxIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5Mzk0MjMzNSwiZXhwIjoyMDA5NTE4MzM1fQ.C9GRRux8dixBbjh_nEHhyZotMqhXSn6OY0BEbmcGyik'
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

#example of data that could be input into the 'Player' table
data = {
    'ID' : 3 , #primary key and must be unique
    'first_name' : 'Kaden',
    'last_name' : 'Ramirez',
    'codename' : 'Eagleye' # must be unique
}

#prints all the data in the 'Player' table
print(supabase.table('Player').select('*').execute().data)

#inserts data into the player table
#supabase.table('Player').insert(data).execute()

#deletes data where 'ID' is equal to 3
#supabase.table('Player').delete().eq('ID', 3).execute()

#updates the Player table entry codename that has 'ID' = 2 to 'FunnyName'
#supabase.table('Player').update({'codename' : 'FunnyName'}).eq('ID', 2).execute()