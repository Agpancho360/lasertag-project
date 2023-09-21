# Import module
from tkinter import *
 
# Create object
splash_root = Tk()
 
# Adjust size
splash_root.geometry("200x200")
 
# Set Label
splash_label = Label(splash_root, text="Splash Screen", font=18)
splash_label.pack()
 
# main window function
 
 
def main():
    # Create object
    root = Tk()
 
    # Adjust size
    root.geometry("400x400")
 
 
# Call main function
main()
 
# Execute tkinter
mainloop()