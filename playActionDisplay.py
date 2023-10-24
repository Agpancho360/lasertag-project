import dataBase
import tkinter

data = [list(row.values()) for row in dataBase.getRedPlayerData()]
table_frame =None
def createRedPlayerFrame(parent, team_name, background_color, border_color):
        global redFrame
        redFrame = tkinter.Frame(parent, bg=background_color, bd=5)
        redFrame.pack(side = "left")
        #table_frame.grid(row=0, column=0, padx=40, pady=40)
        print("Table frame created")
        
        # Create empty rows
        num_empty_rows = 10
        for i in range(num_empty_rows):
            for j in range(2):
                label = tkinter.Label(redFrame, text="")
                label.grid(row=i + 2, column=j)
                label.config(bg = background_color)
        updateTableRed(redFrame)

        return redFrame


def updateTableRed(redFrame):
    background_color = "#e23b4a"
    # Clear existing rows in the table
    for widget in redFrame.winfo_children():
        widget.destroy()

    # Create Team Score
    teamScore = tkinter.Label(redFrame, text="Red Team Score: " + "0 ", font=("Impact", 15), fg ="whitesmoke")
    teamScore.grid(row = 0, column = 0, padx= 25, pady=25)
    teamScore.config(bg = background_color)

    # Create headers
    headers = ["Codename", "Player Score"]
    for j, header in enumerate(headers):
        label = tkinter.Label(redFrame, text=header, font=("Impact", 15), fg ="whitesmoke")
        label.grid(row=1, column=j, padx=25, pady=15)
        label.config(bg = background_color)

    num_empty_rows = 10
    for i in range(num_empty_rows):
        for j in range(2):
            label = tkinter.Label(redFrame, text="")
            label.grid(row=i + 2, column=j)
            label.config(bg = background_color)

    # Get new data from the database
    newData = [list(row.values()) for row in dataBase.getRedPlayerData()]
    # Add new data to the table
    for i, data_row in enumerate(newData, start=2):  # Start at index 2 for data rows
        for j, cell_data in enumerate(data_row):
            label = tkinter.Label(redFrame, text=cell_data, font=("Arial", 10), fg ="whitesmoke")
            label.grid(row=i, column=j)
            label.config(bg = background_color)
     
def createBluePlayerFrame(parent, team_name, background_color, border_color):
    global blueFrame
    blueFrame = tkinter.Frame(parent, bg=background_color, bd=5)
    blueFrame.pack(side = "right")
    print("Blue Table frame created")
        
    # Create empty rows
    num_empty_rows = 10
    for i in range(num_empty_rows):
        for j in range(2):
            label = tkinter.Label(blueFrame, text="")
            label.grid(row=i + 2, column=j)
            label.config(bg=background_color)
    updateTableBlue(blueFrame)

    return blueFrame
       
def updateTableBlue(blueFrame):
    background_color = "#61bbe7"
    # Clear existing rows in the table
    for widget in blueFrame.winfo_children():
        widget.destroy()

    # Create Team Score
    team_score = tkinter.Label(blueFrame, text="Blue Team Score: " + "0 ", font=("Impact", 15), fg="whitesmoke")
    team_score.grid(row=0, column=0, padx=25, pady=25)
    team_score.config(bg=background_color)

    # Create headers
    headers = ["Codename", "Player Score"]
    for j, header in enumerate(headers):
        label = tkinter.Label(blueFrame, text=header, font=("Impact", 15), fg="whitesmoke")
        label.grid(row=1, column=j, padx=25, pady=15)
        label.config(bg=background_color)

    num_empty_rows = 10
    for i in range(num_empty_rows):
        for j in range(2):
            label = tkinter.Label(blueFrame, text="")
            label.grid(row=i + 2, column=j)
            label.config(bg=background_color)

    # Get new data from the database
    new_data = [list(row.values()) for row in dataBase.getBluePlayerData()]
    # Add new data to the table
    for i, data_row in enumerate(new_data, start=2):  # Start at index 2 for data rows
        for j, cell_data in enumerate(data_row):
            label = tkinter.Label(blueFrame, text=cell_data, font=("Arial", 10), fg="whitesmoke")
            label.grid(row=i, column=j)
            label.config(bg=background_color)