# handles user inputs and interactions with the application.
# includes functions for adding new players to either the red or blue team based on user input.
# provides functionality to clear input fields after adding a player.
# responsible for capturing and processing user input data.



# inputs.py
import tkinter as tk
import dataBase
import table_manager

def add_player(team_var, first_name_entry, last_name_entry, codename_entry, id_entry, red_table_frame, blue_table_frame):
    team = team_var.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    codename = codename_entry.get()

    player = dataBase.Player(first_name, last_name, codename, team)
    player.insertPlayer()

    table_manager.update_tables(red_table_frame, blue_table_frame)

    id_entry.delete(0, tk.END)
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    codename_entry.delete(0, tk.END)
