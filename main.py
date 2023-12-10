from tkinter import *
import tkinter as tk
from tkinter import colorchooser
import os
import subprocess
from pygame import mixer
from PIL import Image, ImageTk

def on_validate(char, entry_value):
    # Allow only digits and a single dot
    return char.isdigit() or (char == "." and "." not in entry_value)

def on_submit():
    # Your submit logic here
    pass

def DOS_ON_SUBMIT():
    play_dos_music()

def ping(host):
    try:
        result = subprocess.run(['ping', '-c', '4', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = f"{host} is on means you can DDoS it!."
    except subprocess.CalledProcessError:
        output = f"{host} is off means you cannot DDoS it.."
    
    result_label.config(text=output)

def change_color():
    global color
    color = colorchooser.askcolor()[1]
    root.config(bg=color)
    root.update()

def PING():
    Autorun_button.pack_forget()
    button_ping.pack_forget()
    button_DDoS.pack_forget()
    frame.pack()
    Port.grid_forget()
    label_2.grid_forget()

    def back():
        frame.pack_forget()
        button_ping.pack()
        button_DDoS.pack()
        back.place_forget()
        Autorun_button.pack()

    back = Button(root, text='BACK', font=('Comic Sans', 10), command=back, bg='black', fg='lime')
    back.place(x=850, y=0)
    
    def on_ping_submit():
        host_to_ping = IPA.get()
        ping(host_to_ping)

    submit_button.config(text="Ping IP", command=on_ping_submit)

def play_dos_music():
    # Load and play DOS music once
    dos_music = mixer.Sound(os.path.join(folder_name_Music, "DOS.mp3"))
    dos_music.play()

def DDoS():
    Autorun_button.pack_forget()
    button_ping.pack_forget()
    button_DDoS.pack_forget()
    frame.pack()
    label_1.grid(row=0, column=0)
    IPA.grid(row=0, column=1)
    label_2.grid(row=1, column=0)
    Port.grid(row=1, column=1)

    def back():
        frame.pack_forget()
        button_ping.pack()
        button_DDoS.pack()
        back.place_forget()
        Autorun_button.pack()

    back = Button(root, text='BACK', font=('Comic Sans', 10), command=back, bg='black', fg='lime')
    back.place(x=850, y=0)
    submit_button.config(text="DOS Attack Start", command=DOS_ON_SUBMIT)

def Autorun():
    Autorun_button.pack_forget()
    button_ping.pack_forget()
    button_DDoS.pack_forget()
    frame.pack()
    label_1.grid(row=0, column=0)
    IPA.grid(row=0, column=1)
    label_2.grid(row=1, column=0)
    Port.grid(row=1, column=1)

    def back():
        frame.pack_forget()
        button_ping.pack()
        button_DDoS.pack()
        back.place_forget()
        Autorun_button.pack()

    back = Button(root, text='BACK', font=('Comic Sans', 10), command=back, bg='black', fg='lime')
    back.place(x=850, y=0)
    submit_button.config(text="Autorun DDoS Attack", command=DOS_ON_SUBMIT)

# Initialize the mixer
mixer.init()

current_directory = os.getcwd()
folder_name_Pictures = "Pictures"
folder_name_Music = "Music"

folder_path_Music = os.path.join(current_directory, folder_name_Music)
folder_path_Pictures = os.path.join(current_directory, folder_name_Pictures)

# Load the default music file
music1 = mixer.Sound(os.path.join(folder_name_Music, "Music1.mp3"))

# Set the volume (from 0.0 to 1.0)
music1.set_volume(0.5)

# Start playing the default music with looping
music1.play(-1)

root = tk.Tk()
root.title("Hack Theme Window")
root.geometry("1200x500")
root.resizable(False, False)

hack_image_path = os.path.join(folder_path_Pictures, "Icon.png")
ping_image_path = os.path.join(folder_path_Pictures, "PING.png")
ddos_image_path = os.path.join(folder_path_Pictures, "DDOS.png")
autorun_image_path = os.path.join(folder_path_Pictures, "AUTORUN.png")

hack_image = ImageTk.PhotoImage(Image.open(hack_image_path))
ping_image = ImageTk.PhotoImage(Image.open(ping_image_path))
ddos_image = ImageTk.PhotoImage(Image.open(ddos_image_path))
autorun_image = ImageTk.PhotoImage(Image.open(autorun_image_path))

change_color_button = Button(root, text='change color', font=('Arial', 20), command=change_color, bg='black', fg='lime')
change_color_button.place(x=0, y=450)
color = 'black'
frame = Frame(root, bg=color)
frame.pack()
frame.pack_forget()

# Label and Entry for Input 1
label_1 = tk.Label(frame, text="Import your IP address: ", font=('Arial', 20), fg='lime', bg='black')
label_1.grid(row=0, column=0)

IPA = tk.Entry(frame, font=('Arial', 20), bg='pink', fg='black', validate="key", validatecommand=(root.register(on_validate), "%S", "%P"))
IPA.grid(row=0, column=1)

# Label and Entry for Input 2
label_2 = tk.Label(frame, text="Import your Port number: ", font=('Arial', 20), fg='lime', bg='black')
label_2.grid(row=1, column=0)
Port = tk.Entry(frame, font=('Arial', 20), bg='pink', fg='black', validate="key", validatecommand=(root.register(on_validate), "%S", "%P"))
Port.grid(row=1, column=1)

# Result Label
result_label = tk.Label(frame, text="", font=('Arial', 20), fg='lime', bg='black')
result_label.grid(row=3, column=0)

# Submit Button
submit_button = tk.Button(frame, text="Submit", command=on_submit, font=('Arial', 20), bg='black', fg='lime')
submit_button.grid(row=2, column=0)

button_ping = Button(root, image=ping_image, borderwidth=0, command=PING, bg='black')
button_ping.pack()

button_DDoS = Button(root, image=ddos_image, borderwidth=0, command=DDoS, bg='black')
button_DDoS.pack()

Autorun_button = Button(root, image=autorun_image, borderwidth=0, command=Autorun, bg='black')
Autorun_button.pack()

root.mainloop()
