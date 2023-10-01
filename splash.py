import tkinter as tk
from tkinter import ttk
import dataBase

# Define the main window function
def main_window():
    # Hide the splash screen
    splash_root.withdraw()

    # Create the main application window
    root = tk.Tk()
    root.title("Laser Tag Game")
    root.geometry("1400x600")
    root.configure(bg="black")

    # Function to create a table for displaying player data
    def create_table(parent, team_name, background_color, num_empty_rows=10):
        table_frame = tk.Frame(parent, bg=background_color)
        table_frame.pack(side="left", padx=10)

        # Create labels for table headers
        team_label = tk.Label(table_frame, text=team_name, font=(
            "Impact", 20, "bold"), bg=background_color, fg="white")
        team_label.grid(row=0, column=0, columnspan=4, pady=(10, 5))

        id_label = tk.Label(table_frame, text="ID", font=(
            "Helvetica", 12, "bold"), bg=background_color, fg="white")
        id_label.grid(row=1, column=0)

        first_name_label = tk.Label(table_frame, text="First Name", font=(
            "Helvetica", 12, "bold"), bg=background_color, fg="white")
        first_name_label.grid(row=1, column=1)

        last_name_label = tk.Label(table_frame, text="Last Name", font=(
            "Helvetica", 12, "bold"), bg=background_color, fg="white")
        last_name_label.grid(row=1, column=2)

        codename_label = tk.Label(table_frame, text="Codename", font=(
            "Helvetica", 12, "bold"), bg=background_color, fg="white")
        codename_label.grid(row=1, column=3)

        # Create empty rows
        for i in range(num_empty_rows):
            for j in range(4):
                label = tk.Label(table_frame, text="",
                                 bg=table_frame.cget("bg"), fg="white")
                label.grid(row=i + 2, column=j)

        return table_frame

    # Function to update the player data table
    def update_table(table_frame, data):
        for i, data_row in enumerate(data, start=2):
            for j, data in enumerate(data_row):
                label = tk.Label(table_frame, text=data,
                                 bg=table_frame.cget("bg"), fg="white")
                label.grid(row=i, column=j)

    # Function to add a new player
    def add_player():
        team = team_var.get()  # Get the selected team
        print(team)
        id = id_entry.get()
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        codename = codename_entry.get()

        # Create a Player object and insert it into the database
        player = dataBase.Player(first_name, last_name, codename, team)
        player.insertPlayer()

        # Update the data for the selected team and update the table
        if team == "Red Team":
            red_data.append((id, first_name, last_name, codename))
            update_table(red_table_frame, red_data)
        elif team == "Blue Team":
            blue_data.append((id, first_name, last_name, codename))
            update_table(blue_table_frame, blue_data)

        # Clear the input fields
        id_entry.delete(0, tk.END)
        first_name_entry.delete(0, tk.END)
        last_name_entry.delete(0, tk.END)
        codename_entry.delete(0, tk.END)

    # Default data for Red and Blue teams
    red_data = [
        ("1", "Kaden", "Ramirez", "Eagleye"),
    ]

    blue_data = [
        ("2", "Alex", "Guzman", "Thunder_Lips"),
    ]

    # Create the left frame for input elements
    left_frame = tk.Frame(root, bg="black")
    left_frame.pack(side="left", padx=10)

    # Create a frame for the player entry section with a white background
    player_entry_frame = tk.Frame(left_frame, bg="white", padx=10, pady=10)
    player_entry_frame.grid(row=0, column=0, columnspan=4, pady=(10, 5))

    # Create a Label for the "Player Entry" title
    player_entry_label = tk.Label(player_entry_frame, text="Player Entry", font=(
        "Helvetica", 16, "bold"), bg="white", fg="black")
    player_entry_label.grid(row=0, column=0, columnspan=4, pady=(10, 5))

    # Create input fields and labels for player information
    id_label = tk.Label(player_entry_frame, text="ID:", font=(
        "Helvetica", 12), bg="white", fg="black")
    id_label.grid(row=1, column=0, padx=10)
    id_entry = tk.Entry(player_entry_frame, font=("Helvetica", 12))
    id_entry.grid(row=1, column=1, padx=10)

    first_name_label = tk.Label(player_entry_frame, text="First Name:", font=(
        "Helvetica", 12), bg="white", fg="black")
    first_name_label.grid(row=1, column=2, padx=10)
    first_name_entry = tk.Entry(player_entry_frame, font=("Helvetica", 12))
    first_name_entry.grid(row=1, column=3, padx=10)

    last_name_label = tk.Label(player_entry_frame, text="Last Name:", font=(
        "Helvetica", 12), bg="white", fg="black")
    last_name_label.grid(row=2, column=0, padx=10)
    last_name_entry = tk.Entry(player_entry_frame, font=("Helvetica", 12))
    last_name_entry.grid(row=2, column=1, padx=10)

    codename_label = tk.Label(player_entry_frame, text="Codename:", font=(
        "Helvetica", 12), bg="white", fg="black")
    codename_label.grid(row=2, column=2, padx=10)
    codename_entry = tk.Entry(player_entry_frame, font=("Helvetica", 12))
    codename_entry.grid(row=2, column=3, padx=10)

    # Create a dropdown menu for selecting the team
    team_var = tk.StringVar()
    team_label = tk.Label(player_entry_frame, text="Select Team:", font=(
        "Helvetica", 12), bg="white", fg="black")
    team_label.grid(row=3, column=0, padx=10)
    team_menu = tk.OptionMenu(
        player_entry_frame, team_var, "Red", "Blue")
    team_menu.grid(row=3, column=1, padx=10)

    # Create a button to add a new player
    add_button = tk.Button(player_entry_frame, text="Add Player", font=(
        "Helvetica", 12), command=add_player)
    add_button.grid(row=3, column=2, padx=10, pady=10)

    # Create a label to display the selected team
    selected_team_label = tk.Label(left_frame, text="Selected Team:", font=(
        "Helvetica", 12), bg="black", fg="white")
    selected_team_label.grid(row=4, column=0, columnspan=4, padx=10)

    # Function to update the selected team label when team_var changes
    def update_selected_team_label(*args):
        selected_team_label.config(text="Selected Team: " + team_var.get())

    # Monitor changes to the team_var and call the update_selected_team_label function
    team_var.trace_add("write", update_selected_team_label)

    # Create the right frame for tables
    right_frame = tk.Frame(root, bg="black")
    right_frame.pack(side="right", padx=10)

    # Create the red table on the left side
    red_table_frame = create_table(
        right_frame, team_name="Red Team", background_color="#FF0000")

    # Create the blue table on the right side
    blue_table_frame = create_table(
        right_frame, team_name="Blue Team", background_color="#0000FF")

    # Initialize tables with default data
    update_table(red_table_frame, red_data)
    update_table(blue_table_frame, blue_data)

# Create the splash screen
splash_root = tk.Tk()
splash_root.title("Laser Tag Game")
splash_root.geometry("700x700")

# Load and display an image on the splash screen
img = tk.PhotoImage(file="logo.png")
img = img.subsample(img.width() // 700, img.height() // 700)
splash_label = tk.Label(splash_root, image=img)
splash_label.pack()

# Schedule the main_window function to run after 3 seconds
splash_root.after(3000, main_window)

# Start the main event loop
splash_root.mainloop()
