#sample.py
import customtkinter
import tkinter
from tkinter import ttk
import dataBase
import playerEntry
import blueTable
import redTable
def deleteData(event):
    dataBase.clearData()
    redTable.update_table()
    blueTable.update_table()
def main_window():
    # Hide the splash screen
    splash_root.withdraw()
    # Create the main application window
    root = tkinter.Tk()
    root.title("Laser Tag Game")
    root.geometry("1400x600")
    root.configure(bg="black")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.bind("<F12>",deleteData)
    #creates left frame for playerEntryScreen
    left_frame = customtkinter.CTkFrame(root, fg_color="transparent")
    left_frame.grid(row=0, column=0) #positions left frame to be to the left
    #playerEntrySCreen
    playerEntry.createPlayerEntryFrame(left_frame,"#8d99ae", 5, "#2b2d42")
    #creates right frame for red/blue table frames
    right_frame = customtkinter.CTkFrame(root, fg_color="transparent")
    right_frame.grid(row=0, column=1) #positions left frame to be to the left
    blueTable.createBlueTableFrame(right_frame, "Blue Team", "#61bbe7", "#0577ac")
    redTable.createRedTableFrame (right_frame, "Red Team","#e23b4a","#900A22")

# Create the splash screen
splash_root = tkinter.Tk()
splash_root.title("Laser Tag Game")
splash_root.geometry("700x700")
# Load and display an image on the splash screen
img = tkinter.PhotoImage(file="logo.png")
img = img.subsample(img.width() // 700, img.height() // 700)
splash_label = tkinter.Label(splash_root, image=img)
splash_label.pack()
# Schedule the main_window function to run after 2 seconds
splash_root.after(2000, main_window)
# Start the main event loop
splash_root.mainloop()
