import customtkinter
import tkinter
from tkinter import ttk
import dataBase
import playerEntry
import blueTable
import redTable
import playActionDisplay

def deleteData(event):
    dataBase.clearData()
    redTable.update_table()
    blueTable.update_table()

def countdownTimer(new_window, label, count):
    #destroys window 1 second after zero
    if count < 0:
        label.destroy()
        #new_window.destroy()
        return
    label.config(text=str(count))
    new_window.after(1000, countdownTimer, new_window, label, count - 1)


def createNewWindow(event):
    new_window = tkinter.Toplevel()
    new_window.title("Play Action Screen")
    new_window.geometry("800x600")
    new_window.configure(bg = "black")
    label = tkinter.Label(new_window, text="5", font=("Impact", 45), fg = "whitesmoke", background = 'black')
    label.pack(fill='both', expand=True)
    
    #calls countdown timer upon window creation
    countdownTimer(new_window, label, 5) #window, label, number to start countdown with

    #add red and blue frames to the window
    new_window.after(6000, lambda: playActionDisplay.createRedPlayerFrame(new_window, "Red Team", "#e23b4a", "#900A22"))
     # Creates the blue player frame
    new_window.after(6000, lambda: playActionDisplay.createBluePlayerFrame(new_window, "Blue Team", "#61bbe7", "#0577ac"))

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
    root.bind("<F12>", deleteData)
    root.bind("<F5>", createNewWindow) 

    # creates left frame for playerEntryScreen
    left_frame = customtkinter.CTkFrame(root, fg_color="transparent")
    left_frame.grid(row=0, column=0)  # positions left frame to be to the left
    # playerEntryScreen
    playerEntry.createPlayerEntryFrame(left_frame, "#8d99ae", 5, "#2b2d42")
    # creates right frame for red/blue table frames
    right_frame = customtkinter.CTkFrame(root, fg_color="transparent")
    right_frame.grid(row=0, column=1)  # positions left frame to be to the left
    blueTable.createBlueTableFrame(right_frame, "Blue Team", "#61bbe7", "#0577ac")
    redTable.createRedTableFrame(right_frame, "Red Team", "#e23b4a", "#900A22")

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
