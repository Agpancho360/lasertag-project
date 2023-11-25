#greenTable.py
import dataBase
import customtkinter

data = [list(row.values()) for row in dataBase.getGreenTeamData()]
table_frame = None
def createGreenTableFrame(parent, team_name, background_color, border_color):
        global table_frame
        table_frame = customtkinter.CTkFrame(parent, fg_color=background_color, border_width=5, border_color=border_color)
        table_frame.grid(row=0, column=1, padx=40, pady=40)
        # Create labels and places headers to table
        headers = ["ID", "First Name", "Last Name", "Codename"]
        for j, header in enumerate(headers):
            label = customtkinter.CTkLabel(table_frame, text=header, font=(
                "Impact", 15), text_color="whitesmoke")
            label.grid(row=1, column=j, padx=25, pady=15)
        # Create empty rows
        num_empty_rows = dataBase.getGreenTeamCount() + 1
        for i in range(num_empty_rows):
            for j in range(4):
                label = customtkinter.CTkLabel(table_frame, text="")
                label.grid(row=i + 2, column=j)
        update_table()
        return table_frame

def update_table():
    # Clear existing rows in the table
    for widget in table_frame.winfo_children():
        widget.destroy()

    # Create headers
    headers = ["ID", "First Name", "Last Name", "Codename"]
    for j, header in enumerate(headers):
        label = customtkinter.CTkLabel(table_frame, text=header, font=(
            "Impact", 15), text_color="whitesmoke")
        label.grid(row=1, column=j, padx=25, pady=15)
        
    #creates empty entries
    num_empty_rows = dataBase.getGreenTeamCount() + 1
    for i in range(num_empty_rows):
        for j in range(4):
            label = customtkinter.CTkLabel(table_frame, text="")
            label.grid(row=i + 2, column=j)

    # Get new data from the database
    newData = [list(row.values()) for row in dataBase.getGreenTeamData()]

    # Add new data to the table
    for i, data_row in enumerate(newData, start=2):
        for j, cell_data in enumerate(data_row):
            label = customtkinter.CTkLabel(table_frame, text=cell_data, font=(
                "Arial", 10), text_color="whitesmoke")
            label.grid(row=i, column=j)