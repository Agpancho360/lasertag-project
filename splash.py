from tkinter import *

splash_root = Tk()
splash_root.title("Splash Screen")
splash_root.geometry("700x700")

# Load the image and keep a reference to it
# img = PhotoImage(file="logo.jpg")
splash_label = Label(splash_root, text= "Add image here", font=("Helvetica", 18))
splash_label.pack(pady=20)

def main_window():
    splash_root.destroy()
    root = Tk()
    root.title("Main Window")
    root.geometry("700x700")

# Call the main_window function after 3000 milliseconds (3 seconds)
splash_root.after(3000, main_window)
splash_root.mainloop()
