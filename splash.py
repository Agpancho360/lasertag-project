import tkinter as tk
from tkinter import ttk

def main_window():
    splash_root.withdraw()
    root = tk.Toplevel()
    root.title("Laser Tag Game")
    root.geometry("800x800")
    root.configure(bg="black")

    def create_table(parent, row_offset, team_name, background_color, num_empty_rows=10):
        table_frame = tk.Frame(parent, bg=background_color)
        table_frame.grid(row=row_offset - 1, column=0, columnspan=4, pady=(10, 5), sticky="w")

        team_label = tk.Label(table_frame, text=team_name, font=("Impact", 20, "bold"), bg=background_color, fg="white")
        team_label.grid(row=0, column=0, columnspan=4, pady=(10, 5))

        id_label = tk.Label(table_frame, text="ID", font=("Helvetica", 12, "bold"), bg=background_color, fg="white")
        id_label.grid(row=1, column=0)

        first_name_label = tk.Label(table_frame, text="First Name", font=("Helvetica", 12, "bold"), bg=background_color, fg="white")
        first_name_label.grid(row=1, column=1)

        last_name_label = tk.Label(table_frame, text="Last Name", font=("Helvetica", 12, "bold"), bg=background_color, fg="white")
        last_name_label.grid(row=1, column=2)

        codename_label = tk.Label(table_frame, text="Codename", font=("Helvetica", 12, "bold"), bg=background_color, fg="white")
        codename_label.grid(row=1, column=3)

        # Create empty rows
        for i in range(num_empty_rows):
            for j in range(4):
                label = tk.Label(table_frame, text="", bg=table_frame.cget("bg"), fg="white")
                label.grid(row=i + 2, column=j)

        return table_frame

    def update_table(table_frame, data):
        for i, data_row in enumerate(data, start=2):
            for j, data in enumerate(data_row):
                label = tk.Label(table_frame, text=data, bg=table_frame.cget("bg"), fg="white")
                label.grid(row=i, column=j)

    def add_player():
        team = team_var.get()
        new_id = id_entry.get()
        new_first_name = first_name_entry.get()
        new_last_name = last_name_entry.get()
        new_codename = codename_entry.get()

        if team == "Red Team":
            red_data.append((new_id, new_first_name, new_last_name, new_codename))
            update_table(red_table_frame, red_data)
        elif team == "Blue Team":
            blue_data.append((new_id, new_first_name, new_last_name, new_codename))
            update_table(blue_table_frame, blue_data)

        id_entry.delete(0, tk.END)
        first_name_entry.delete(0, tk.END)
        last_name_entry.delete(0, tk.END)
        codename_entry.delete(0, tk.END)

    red_data = [
        ("1", "Kaden", "Ramirez", "Eagleye"),
    ]

    blue_data = [
        ("2", "Alex", "Guzman", "Thunder_Lips"),
    ]

    red_table_frame = create_table(root, row_offset=1, team_name="Red Team", background_color="#FF0000")
    blue_table_frame = create_table(root, row_offset=6, team_name="Blue Team", background_color="#0000FF")

    input_frame = tk.Frame(root, bg="black")
    input_frame.grid(row=14, column=0, columnspan=4, pady=(10, 5))

    id_label = tk.Label(input_frame, text="ID:", font=("Helvetica", 12), bg="black", fg="white")
    id_label.grid(row=0, column=0, padx=10)
    id_entry = tk.Entry(input_frame, font=("Helvetica", 12))
    id_entry.grid(row=0, column=1, padx=10)

    first_name_label = tk.Label(input_frame, text="First Name:", font=("Helvetica", 12), bg="black", fg="white")
    first_name_label.grid(row=0, column=2, padx=10)
    first_name_entry = tk.Entry(input_frame, font=("Helvetica", 12))
    first_name_entry.grid(row=0, column=3, padx=10)

    last_name_label = tk.Label(input_frame, text="Last Name:", font=("Helvetica", 12), bg="black", fg="white")
    last_name_label.grid(row=1, column=0, padx=10)
    last_name_entry = tk.Entry(input_frame, font=("Helvetica", 12))
    last_name_entry.grid(row=1, column=1, padx=10)

    codename_label = tk.Label(input_frame, text="Codename:", font=("Helvetica", 12), bg="black", fg="white")
    codename_label.grid(row=1, column=2, padx=10)
    codename_entry = tk.Entry(input_frame, font=("Helvetica", 12))
    codename_entry.grid(row=1, column=3, padx=10)

    team_var = tk.StringVar()
    team_var.set("Red Team")
    team_label = tk.Label(input_frame, text="Select Team:", font=("Helvetica", 12), bg="black", fg="white")
    team_label.grid(row=2, column=0, padx=10)
    team_menu = tk.OptionMenu(input_frame, team_var, "Red Team", "Blue Team")
    team_menu.grid(row=2, column=1, padx=10)

    add_button = tk.Button(input_frame, text="Add Player", font=("Helvetica", 12), command=add_player)
    add_button.grid(row=2, column=2, padx=10, pady=10)

    # Initialize tables with default data
    update_table(red_table_frame, red_data)
    update_table(blue_table_frame, blue_data)

splash_root = tk.Tk()
splash_root.title("Laser Tag Game")
splash_root.geometry("700x700")

img = tk.PhotoImage(file="logo.png")
img = img.subsample(img.width() // 700, img.height() // 700)

splash_label = tk.Label(splash_root, image=img)
splash_label.pack()

splash_root.after(3000, main_window)

splash_root.mainloop()
