import customtkinter
import tkinter
from tkinter import ttk
import dataBase


def main_window():
    # # initalizes data for table use
    red_team_data = [list(row.values()) for row in dataBase.getRedTeamData()]
    blue_team_data = [list(row.values()) for row in dataBase.getBlueTeamData()]

    # Hide the splash screen
    splash_root.withdraw()
    # Create the main application window
    root = tkinter.Tk()
    root.title("Laser Tag Game")
    root.geometry("1400x600")
    root.configure(bg="black")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

    def create_table(parent, team_name, column, background_color, border_color):
        table_frame = customtkinter.CTkFrame(
            parent, fg_color=background_color, border_width=5, border_color=border_color)
        table_frame.grid(row=0, column=column, padx=40, pady=40)
        # Create labels for table headers
        team_label = customtkinter.CTkLabel(
            table_frame, text=team_name, font=("Impact", 25), text_color="whitesmoke")
        id_label = customtkinter.CTkLabel(
            table_frame, text="ID", font=("Impact", 15), text_color="whitesmoke")
        first_name_label = customtkinter.CTkLabel(
            table_frame, text="First Name", font=("Impact", 15), text_color="whitesmoke")
        last_name_label = customtkinter.CTkLabel(
            table_frame, text="Last Name", font=("Impact", 15), text_color="whitesmoke")
        codename_label = customtkinter.CTkLabel(
            table_frame, text="Codename", font=("Impact", 15), text_color="whitesmoke")
        # places labels to team table
        team_label.grid(row=0, column=0, columnspan=4, pady=15)
        id_label.grid(row=1, column=0, padx=25, pady=15)
        first_name_label.grid(row=1, column=1, padx=25, pady=15)
        last_name_label.grid(row=1, column=2, padx=25, pady=15)
        codename_label.grid(row=1, column=3, padx=25, pady=15)

        # Create empty rows
        num_empty_rows = 10
        for i in range(num_empty_rows):
            for j in range(4):
                label = customtkinter.CTkLabel(table_frame, text="")
                label.grid(row=i + 2, column=j)

        return table_frame
    # Function to update the player data table

    def update_table(table_frame, data):
        for i, data_row in enumerate(data, start=2):
            for j, cell_data in enumerate(data_row):
                label = customtkinter.CTkLabel(table_frame, text=cell_data, font=(
                    "Arial", 10), text_color="whitesmoke")
                label.grid(row=i, column=j)

    def add_player():
        team = team_entry.get()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        codename = codename_entry.get()
        # Create a Player object and insert it into the database
        player = dataBase.Player(first_name, last_name, codename, team)
        player.insertPlayer()

        # Update the data for the selected team and update the table
        if team == "Red":
            red_team_data = [list(row.values())
                             for row in dataBase.getRedTeamData()]
            update_table(red_table_frame, red_team_data)
        elif team == "Blue":
            blue_team_data = [list(row.values())
                              for row in dataBase.getBlueTeamData()]
            update_table(blue_table_frame, blue_team_data)

        # Clear the input fields
        # id_entry.delete(0, customtkinter.CTkEntry.END)
        first_name_entry.delete(0, customtkinter.CTkEntry.END)
        last_name_entry.delete(0, customtkinter.CTkEntry.END)
        codename_entry.delete(0, customtkinter.CTkEntry.END)
   # **************************************Left Frame *******************************************************
    left_frame = customtkinter.CTkFrame(root, fg_color="transparent")
    left_frame.grid(row=0, column=0)
    # **************************************Player Entry Screen *******************************************************
    player_entry_frame = customtkinter.CTkFrame(left_frame,fg_color="#8d99ae", border_width=5, border_color="#2b2d42")
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
        player_entry_frame, values=["Blue", "Red"])
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

    # **************************************Right frame *******************************************************
    right_frame = customtkinter.CTkFrame(root, fg_color="transparent")
    right_frame.grid(row=0, column=1)
    # **************************************Red Table Frame *******************************************************
    red_table_frame = create_table(
        right_frame, "Red Team", 0, "#e23b4a", "#900A22")
    # **************************************Blue Table Frame *******************************************************
    blue_table_frame = create_table(
        right_frame, "Blue Team", 1, "#61bbe7", "#0577ac")
    update_table(red_table_frame, red_team_data)
    update_table(blue_table_frame, blue_team_data)


# Create the splash screen
splash_root = tkinter.Tk()
splash_root.title("Laser Tag Game")
splash_root.geometry("700x700")

# Load and display an image on the splash screen
img = tkinter.PhotoImage(file="logo.png")
img = img.subsample(img.width() // 700, img.height() // 700)
splash_label = tkinter.Label(splash_root, image=img)
splash_label.pack()

# Schedule the main_window function to run after 3 seconds
splash_root.after(3000, main_window)

# Start the main event loop
splash_root.mainloop()
