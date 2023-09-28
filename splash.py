import tkinter as tk
from tkinter import PhotoImage

def main_window():
    splash_root.destroy()
    root = tk.Tk()
    root.title("Main Window")
    root.geometry("700x700")

# Create the splash screen window
splash_root = tk.Tk()
splash_root.title("Splash Screen")
splash_root.geometry("700x700")

# Load the image and resize it to fit the 700x700 window
img = PhotoImage(file="logo.png")
img = img.subsample(img.width() // 700, img.height() // 700)

splash_label = tk.Label(splash_root, image=img)
splash_label.pack()

# Call the main_window function after 3000 milliseconds (3 seconds)
splash_root.after(3000, main_window)

splash_root.mainloop()
