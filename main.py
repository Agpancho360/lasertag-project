import customtkinter
import tkinter
from tkinter import ttk
import dataBase
import playerEntry
import greenTable
import redTable
import playActionDisplay
import pygame
import socket
import time


def updateTables():
    print("Updating tables...")
    playActionDisplay.updateTableGreen(playActionDisplay.greenFrame)
    playActionDisplay.updateTableRed(playActionDisplay.redFrame)
    playActionDisplay.updateInfo(dataBase.getEventString())


def sendCodesLoop(window):
    clientAddressPort = ("127.0.0.1", 7500)
    testPort = ("127.0.0.1", 7504)
    UDPClientSocketTransmit = socket.socket(
        family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPClientSocketTransmit.bind(testPort)
    msg1 = str(202)
    msg2 = str(221)
    msg3 = str(53)
    i = 0
    while (i <= 30):
        if (i < 5):
            UDPClientSocketTransmit.sendto(
                str.encode(str(msg1)), clientAddressPort)
        elif (30 > i >= 5):
            UDPClientSocketTransmit.sendto(
                str.encode(str(msg3)), clientAddressPort)
        else:
            UDPClientSocketTransmit.sendto(
                str.encode(str(msg2)), clientAddressPort)
        window.after(1000, updateTables)
        window.after(1000, window.update_idletasks)
        i += 1


def deleteData(event):
    dataBase.clearData()
    redTable.update_table()
    greenTable.update_table()


def sound():
    pygame.mixer.init()
    pygame.mixer.music.load("./Track01.mp3")
    pygame.mixer.music.play()


def intro(duration):
    pygame.mixer.init()
    pygame.mixer.music.load("./Track01.mp3")
    pygame.mixer.music.play()

    start_time = pygame.time.get_ticks()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(60)

        elapsed_time = pygame.time.get_ticks() - start_time

        if elapsed_time >= duration * 1000:
            pygame.mixer.music.stop()
            break


def countdownTimer(new_window, label, count):
    if count < 0:
        label.destroy()
        return
    label.config(text=str(count))
    new_window.after(1000, countdownTimer, new_window, label, count - 1)


def createTimerFrame(new_window):
    count = 360  # 6 minutes * 60 seconds
    countdown_label = tkinter.Label(new_window, text="6:00", font=(
        "Impact", 20), fg="whitesmoke", background='black')
    countdown_label.pack(pady=10)

    def updateCountdown():
        nonlocal count
        if count > 0:
            minutes = count // 60
            seconds = count % 60
            time_str = f"{minutes:02}:{seconds:02}"
            countdown_label.config(text=time_str)
            count -= 1
            new_window.after(1000, updateCountdown)
        else:
            countdown_label.destroy()
            new_window.destroy()

    updateCountdown()


def playSoundAndCreateWindow(event):
    sound()
    new_window = tkinter.Toplevel()
    new_window.title("Play Action Screen")
    new_window.attributes('-fullscreen', True)
    new_window.configure(bg="black")
    label = tkinter.Label(new_window, text="5", font=(
        "Impact", 45), fg="whitesmoke", background='black')
    label.pack(fill='both', expand=True)

    timerCount = 2
    countdownTimer(new_window, label, timerCount)

    new_window.after(timerCount * 1000 + 1000,
                     lambda: playActionDisplay.createRedPlayerFrame(new_window, "Red Team", "#e23b4a"))
    new_window.after(timerCount * 1000 + 1000,
                     lambda: playActionDisplay.createGreenPlayerFrame(new_window, "Green Team", "#00CF06"))
    new_window.after(timerCount * 1000 + 1000,lambda: playActionDisplay.createEventFrame(new_window, "Events", "#051ffa"))
    new_window.after(timerCount * 1000 + 1000, lambda: createTimerFrame(new_window))
    new_window.after((timerCount + 15) * 1000,
                     lambda: sendCodesLoop(new_window))


def main_window():
    splash_root.withdraw()
    root = tkinter.Tk()
    root.title("Laser Tag Game")
    root.geometry("1400x600")
    root.configure(bg="black")
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.bind("<F12>", deleteData)
    root.bind("<F5>", playSoundAndCreateWindow)
    left_frame = customtkinter.CTkFrame(root, fg_color="transparent")
    left_frame.grid(row=0, column=0)
    playerEntry.createPlayerEntryFrame(left_frame, "#8d99ae", 5, "#2b2d42")
    right_frame = customtkinter.CTkFrame(root, fg_color="transparent")
    right_frame.grid(row=0, column=1)
    greenTable.createGreenTableFrame(
        right_frame, "Green Team", "#00CF06", "#05FF0D")
    redTable.createRedTableFrame(right_frame, "Red Team", "#e23b4a", "#900A22")


splash_root = tkinter.Tk()
splash_root.title("Laser Tag Game")
splash_root.attributes('-fullscreen', True)
splash_root.configure(bg="black")
img = tkinter.PhotoImage(file="logo.png")
img = img.subsample(img.width() // 700, img.height() // 700)
splash_label = tkinter.Label(splash_root, image=img)
splash_label.pack()
intro(3)
splash_root.after(2000, main_window)
splash_root.mainloop()
