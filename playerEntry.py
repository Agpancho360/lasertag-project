#playerEntry.py
import customtkinter
import dataBase
import redTable
import greenTable
import playActionDisplay



def createPlayerEntryFrame(parent,backgroundColor, borderWidth, borderColor):
    global first_name_entry, last_name_entry, codename_entry, team_entry
    player_entry_frame = customtkinter.CTkFrame(parent, fg_color= backgroundColor,border_width= borderWidth, border_color=borderColor)
    player_entry_frame.grid(row=0, column=0)
    # creates labels, entry, and button for player entry screen
    player_entry_label = customtkinter.CTkLabel(
        player_entry_frame, text="Player Entry", font=("Impact", 25), text_color="whitesmoke")
    first_name_label = customtkinter.CTkLabel(
        player_entry_frame, text="First Name:", font=("Impact", 15), text_color="whitesmoke")
    first_name_entry = customtkinter.CTkEntry(
        player_entry_frame, placeholder_text="First Name")
    last_name_label = customtkinter.CTkLabel(
        player_entry_frame, text="Last Name:", font=("Impact", 15), text_color="whitesmoke")
    last_name_entry = customtkinter.CTkEntry(
        player_entry_frame, placeholder_text="Last Name")
    codename_label = customtkinter.CTkLabel(
        player_entry_frame, text="Codename:", font=("Impact", 15), text_color="whitesmoke")
    codename_entry = customtkinter.CTkEntry(
        player_entry_frame, placeholder_text="Codename")
    team_label = customtkinter.CTkLabel(
        player_entry_frame, text="Select Team:", font=("Impact", 15), text_color="whitesmoke")
    team_entry = customtkinter.CTkOptionMenu(
        player_entry_frame, values=["Green", "Red"])
    submitButton = customtkinter.CTkButton(
        player_entry_frame, text="Submit", corner_radius=  25, command=add_player)
    # places items onto player entry screen
    player_entry_label.grid(row=0, column=0, columnspan=2, padx=25, pady=15)
    first_name_label.grid(row=1, column=0, padx=25, pady=15)
    first_name_entry.grid(row=1, column=1, padx=25, pady=15)
    last_name_label.grid(row=2, column=0, padx=25, pady=15)
    last_name_entry.grid(row=2, column=1, padx=25, pady=15)
    codename_label.grid(row=3, column=0, padx=25, pady=15)
    codename_entry.grid(row=3, column=1, padx=25, pady=15)
    team_label.grid(row=4, column=0, padx=25, pady=15)
    team_entry.grid(row=4, column=1, padx=25, pady=15)
    submitButton.grid(row=5, column=0, columnspan=2, padx=25, pady=15)

    return player_entry_frame
def add_player():
        
    team = team_entry.get()
    if((int(dataBase.getRedTeamCount()) < 15 and team == 'Red') or (int(dataBase.getGreenTeamCount()) < 15 and team == 'Green')):
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        codename = codename_entry.get()
        # Create a Player object and insert it into the database
        player = dataBase.Player(first_name, last_name, codename, team)
        player.insertPlayer()
        if team == "Red":
            redTable.update_table()
            playActionDisplay.updateTableRed(playActionDisplay.redFrame)
        elif team == "Green":
            greenTable.update_table()
            playActionDisplay.updateTablegreen(playActionDisplay.greenFrame)

    else:
        print('There are already 15 players on this team')

    # Clear the input fields
    first_name_entry.delete(0, customtkinter.END)
    last_name_entry.delete(0,customtkinter.END)
    codename_entry.delete(0, customtkinter.END)