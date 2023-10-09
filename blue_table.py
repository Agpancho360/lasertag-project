# blue_table.py
import tkinter as tk

def create_blue_table(parent, team_name, background_color, num_empty_rows=10):
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

def update_blue_table(table_frame, data):
    for i, data_row in enumerate(data, start=2):
        for j, cell_data in enumerate(data_row):
            label = tk.Label(table_frame, text=cell_data,
                             bg=table_frame.cget("bg"), fg="white")
            label.grid(row=i, column=j)
