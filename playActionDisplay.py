import dataBase
import tkinter

data = [list(row.values()) for row in dataBase.getRedPlayerData()]

def createRedPlayerFrame(parent, team_name, background_color):
        global redFrame
        redFrame = tkinter.Frame(parent, bg=background_color, bd=5)
        redFrame.pack(side = "left")
        #table_frame.grid(row=0, column=0, padx=40, pady=40)
        print("Table frame created")
        
        # Create empty rows
        num_empty_rows = dataBase.getRedTeamCount() + 1
        for i in range(num_empty_rows):
            for j in range(2):
                label = tkinter.Label(redFrame, text="")
                label.grid(row=i + 2, column=j)
                label.config(bg = background_color)
        updateTableRed(redFrame)

        return redFrame


def updateTableRed(redFrame):
    background_color = "#e23b4a"
    
    # Create Team Score
    teamScore = tkinter.Label(redFrame, text="Red Team Score: " + str(dataBase.getRedTeamScore()), font=("Impact", 15), fg="whitesmoke")
    teamScore.grid(row=0, column=0, padx=25, pady=25)
    teamScore.config(bg=background_color)

    # Create headers
    headers = ["Codename", "Player Score"]
    for j, header in enumerate(headers):
        label = tkinter.Label(redFrame, text=header, font=("Impact", 15), fg="whitesmoke")
        label.grid(row=1, column=j, padx=25, pady=15)
        label.config(bg=background_color)

    # Get new data from the database
    newData = [list(row.values()) for row in dataBase.getRedPlayerData()]

    # Destroy existing labels
    for widget in redFrame.winfo_children():
        if widget.grid_info()["row"] >= 2:  # Exclude Team Score and headers
            widget.destroy()

    # Add new data to the table
    for i, data_row in enumerate(newData, start=2):
        for j, cell_data in enumerate(data_row):
            label = tkinter.Label(redFrame, text=cell_data, font=("Arial", 10), fg="whitesmoke")
            label.grid(row=i, column=j)
            label.config(bg=background_color)
     
def createGreenPlayerFrame(parent, team_name, background_color):
    global greenFrame
    greenFrame = tkinter.Frame(parent, bg=background_color, bd=5)
    greenFrame.pack(side = "right")
    print("Green Table frame created")
        
    # Create empty rows
    num_empty_rows = dataBase.getGreenTeamCount() + 1
    for i in range(num_empty_rows):
        for j in range(2):
            label = tkinter.Label(greenFrame, text="")
            label.grid(row=i + 2, column=j)
            label.config(bg=background_color)
    updateTableGreen(greenFrame)

    return greenFrame
       
def updateTableGreen(greenFrame):
    background_color = "#00CF06"
    
    # Create Team Score
    team_score = tkinter.Label(greenFrame, text="Green Team Score: " + str(dataBase.getGreenTeamScore()), font=("Impact", 15), fg="whitesmoke")
    team_score.grid(row=0, column=0, padx=25, pady=25)
    team_score.config(bg=background_color)

    # Create headers
    headers = ["Codename", "Player Score"]
    for j, header in enumerate(headers):
        label = tkinter.Label(greenFrame, text=header, font=("Impact", 15), fg="whitesmoke")
        label.grid(row=1, column=j, padx=25, pady=15)
        label.config(bg=background_color)

    # Get new data from the database
    new_data = [list(row.values()) for row in dataBase.getGreenPlayerData()]

    # Destroy existing labels
    for widget in greenFrame.winfo_children():
        if widget.grid_info()["row"] >= 2:  # Exclude Team Score and headers
            widget.destroy()

    # Add new data to the table
    for i, data_row in enumerate(new_data, start=2):
        for j, cell_data in enumerate(data_row):
            label = tkinter.Label(greenFrame, text=cell_data, font=("Arial", 10), fg="whitesmoke")
            label.grid(row=i, column=j)
            label.config(bg=background_color)

def createEventFrame(parent, title, background_color):
    global event_frame
    event_frame = tkinter.Frame(parent, bg=background_color, bd=5)

    # Create a Text widget for displaying information
    info_text = tkinter.Text(event_frame, height=10, width=40, font=("Arial", 10), wrap="word", bg=background_color, state='disabled')
    info_text.pack(pady=10, expand=True)

    # Center the frame using place
    event_frame.place(relx=0.5, rely=0.5, anchor="center")

    return event_frame

def updateInfo(new_info):
    global event_frame
    # Get the Text widget from the event frame
    info_text = event_frame.winfo_children()[0]

    # Set the state to normal, insert new information, and set it back to disabled
    info_text.config(state='normal')
    info_text.insert(tkinter.END, new_info + "\n")
    info_text.config(state='disabled')

    # Scroll to the end to show the latest information
    info_text.see(tkinter.END)






