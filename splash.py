# initializes the splash screen
# displays a logo image for a few seconds before launching the main window.
# main_window function is scheduled to run after the splash screen, creating the main application window.

import tkinter as tk
import red_table
import blue_table
import inputs
import dataBase

# Define the main window function
def main_window():
    # Initializes data for table use
    red_team_data = [list(row.values()) for row in dataBase.getRedTeamData()]  # You can load this data from your database if needed
    blue_team_data = [list(row.values()) for row in dataBase.getBlueTeamData()]  # You can load this data from your database if needed

    # Hide the splash screen
    splash_root.withdraw()

    # Create the main application window
    root = tk.Tk()
    root.title("Laser Tag Game")
    root.geometry("2000x2000")
    root.configure(bg="black")

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
        "Helvetica", 12), command=lambda: inputs.add_player(team_var, first_name_entry, last_name_entry, codename_entry, id_entry, red_table_frame, blue_table_frame))
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
    red_table_frame = red_table.create_red_table(
        right_frame, team_name="Red Team", background_color="#FF0000")

    # Create the blue table on the right side
    blue_table_frame = blue_table.create_blue_table(
        right_frame, team_name="Blue Team", background_color="#0000FF")

    # Initialize tables with default data
    red_table.update_red_table(red_table_frame, red_team_data)
    blue_table.update_blue_table(blue_table_frame, blue_team_data)

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