#redTable.py
import dataBase
import customtkinter

red_team_data = [list(row.values()) for row in dataBase.getRedTeamData()]
table_frame =None
def createRedTableFrame(parent, team_name, background_color, border_color):
        global table_frame
        table_frame = customtkinter.CTkFrame(parent, fg_color=background_color, border_width=5, border_color=border_color)
        table_frame.grid(row=0, column=0, padx=40, pady=40)
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
        update_table(table_frame,red_team_data)

        return table_frame


def update_table(table_frame,data):
    for i, data_row in enumerate(data, start=2):
        for j, cell_data in enumerate(data_row):
            label = customtkinter.CTkLabel(table_frame, text=cell_data, font=(
                "Arial", 10), text_color="whitesmoke")
            label.grid(row=i, column=j)