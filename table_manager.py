# responsible for managing and updating the red and blue team tables.
# includes functions to create the tables, initialize them with default data, and update them with data from your database.



# table_manager.py
import tkinter as tk
import red_table
import blue_table
import dataBase

def create_tables(parent):
    red_team_data = [list(row.values()) for row in dataBase.getRedTeamData()]  # Load this data from your database if needed
    blue_team_data = [list(row.values()) for row in dataBase.getBlueTeamData()]  # Load this data from your database if needed

    # Create the red table on the left side
    red_table_frame = red_table.create_red_table(
        parent, team_name="Red Team", background_color="#FF0000")

    # Create the blue table on the right side
    blue_table_frame = blue_table.create_blue_table(
        parent, team_name="Blue Team", background_color="#0000FF")

    # Initialize tables with default data
    red_table.update_red_table(red_table_frame, red_team_data)
    blue_table.update_blue_table(blue_table_frame, blue_team_data)

    return red_table_frame, blue_table_frame

def update_tables(red_table_frame, blue_table_frame):
    red_team_data = [list(row.values()) for row in dataBase.getRedTeamData()]
    blue_team_data = [list(row.values()) for row in dataBase.getBlueTeamData()]

    red_table.update_red_table(red_table_frame, red_team_data)
    blue_table.update_blue_table(blue_table_frame, blue_team_data)
