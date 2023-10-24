import dataBase
import tkinter

data = [list(row.values()) for row in dataBase.getRedPlayerData()]
table_frame =None
def createRedPlayerFrame(parent, team_name, background_color, border_color):
        global table_frame
        table_frame = tkinter.Frame(parent, bg=background_color, bd=5)
        table_frame.pack()
        #table_frame.grid(row=0, column=0, padx=40, pady=40)
        print("Table frame created")
         # Create labels and places headers to table
        headers = ["Codename", "Player Score"]
        for j, header in enumerate(headers):
            label = tkinter.Label(table_frame, text="5", font=("Impact", 15), fg = "whitesmoke", background = background_color)
            label.grid(row=1, column=j, padx=25, pady=15)
            label.config(bg = background_color)
        
        # Create empty rows
        num_empty_rows = 10
        for i in range(num_empty_rows):
            for j in range(2):
                label = tkinter.Label(table_frame, text="")
                label.grid(row=i + 2, column=j)
                label.config(bg = background_color)
        update_table_red()

        return table_frame


def update_table_red():
    background_color = "#e23b4a"
    # Clear existing rows in the table
    for widget in table_frame.winfo_children():
        widget.destroy()

    # Create Team Score
    teamScore = tkinter.Label(table_frame, text="Red Team Score: " + "0 ", font=("Impact", 15), fg ="whitesmoke")
    teamScore.grid(row = 0, column = 0, padx= 25, pady=25)
    teamScore.config(bg = background_color)

    # Create headers
    headers = ["Codename", "Player Score"]
    for j, header in enumerate(headers):
        label = tkinter.Label(table_frame, text=header, font=("Impact", 15), fg ="whitesmoke")
        label.grid(row=1, column=j, padx=25, pady=15)
        label.config(bg = background_color)

    num_empty_rows = 10
    for i in range(num_empty_rows):
        for j in range(2):
            label = tkinter.Label(table_frame, text="")
            label.grid(row=i + 2, column=j)
            label.config(bg = background_color)

    # Get new data from the database
    newData = [list(row.values()) for row in dataBase.getRedPlayerData()]
    # Add new data to the table
    for i, data_row in enumerate(newData, start=2):  # Start at index 2 for data rows
        for j, cell_data in enumerate(data_row):
            label = tkinter.Label(table_frame, text=cell_data, font=("Arial", 10), fg ="whitesmoke")
            label.grid(row=i, column=j)
            label.config(bg = background_color)
