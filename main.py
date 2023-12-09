from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import colorchooser
import os

current_directory = os.getcwd()
folder_name = "Pictures"
folder_path = os.path.join(current_directory, folder_name)


def validate_input(char):
    return char.isdigit() or char == "."
def validate_input1(char):
    return char.isdigit()

def on_submit():
    # Write your code here and delete the 'pass'
    pass

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
    def cancle():
        frame.pack_forget()
        button_ping.pack()
        button_DDoS.pack()
        Cancle.place_forget()
        Autorun_button.pack()
    Cancle = Button(root, text='CANCEL', font=('Comic Sans', 10), command=cancle)
    Cancle.place(x=730, y=0)

def DDoS():
    Autorun_button.pack_forget()
    button_ping.pack_forget()
    button_DDoS.pack_forget()
    frame.pack()
    label_1.grid(row=0, column=0)
    IPA.grid(row=0, column=1)
    label_2.grid(row=1, column=0)
    Port.grid(row=1, column=1)

    def cancle():
        frame.pack_forget()
        button_ping.pack()
        button_DDoS.pack()
        Cancle.place_forget()
        Autorun_button.pack()

    Cancle = Button(root, text='CANCEL', font=('Comic Sans', 10), command=cancle)
    Cancle.place(x=730, y=0)

def Autorun():
    Autorun_button.pack_forget()
    button_ping.pack_forget()
    button_DDoS.pack_forget()
    frame.pack()
    label_1.grid(row=0, column=0)
    IPA.grid(row=0, column=1)
    label_2.grid(row=1, column=0)
    Port.grid(row=1, column=1)

    def cancle():
        frame.pack_forget()
        button_ping.pack()
        button_DDoS.pack()
        Cancle.place_forget()
        Autorun_button.pack()

    Cancle = Button(root, text='CANCEL', font=('Comic Sans', 10), command=cancle)
    Cancle.place(x=730, y=0)

root = tk.Tk()
root.title("Input Window")
root.geometry("800x500")

hack_image_path = os.path.join(folder_path, "hacked.png")
ping_image_path = os.path.join(folder_path, "PING.png")
ddos_image_path = os.path.join(folder_path, "DDoS.png")
autorun_image_path = os.path.join(folder_path, "Autorun.png")

hack_image = PhotoImage(file=hack_image_path)
ping_image = PhotoImage(file=ping_image_path)
ddos_image = PhotoImage(file=ddos_image_path)
autorun_image = PhotoImage(file=autorun_image_path)

root.resizable(False, False)
root.iconphoto(True, hack_image)

change_color_button = Button(root, text='change color', font=('Arial', 20), command=change_color)
change_color_button.place(x=0, y=450)
color = 'white'
frame = Frame(root, bg=color)
frame.pack()
frame.pack_forget()

# Label and Entry for Input 1
label_1 = tk.Label(frame, text="Import your IP address: ", font=('Arial', 20), fg='lime', bg='black')
label_1.grid(row=0, column=0)

validate_input_1 = root.register(validate_input)
IPA = tk.Entry(frame, validate="key", validatecommand=(validate_input_1, "%S"), font=('Arial', 20), bg='pink')
IPA.grid(row=0, column=1)

# Label and Entry for Input 2
label_2 = tk.Label(frame, text="Import your Port number: ", font=('Arial', 20), fg='lime', bg='black')
label_2.grid(row=1, column=0)
validate_input_2 = root.register(validate_input1)
Port = tk.Entry(frame, validate="key", validatecommand=(validate_input_2, "%S"), font=('Arial', 20), bg='pink')
Port.grid(row=1, column=1)

# Submit Button
submit_button = tk.Button(frame, text="Ping IP", command=on_submit, font=('Arial', 20))
submit_button.grid(row=2, column=0)

button_ping = Button(root, image=ping_image, command=PING, borderwidth=0)
button_ping.pack()

button_DDoS = Button(root, image=ddos_image, borderwidth=0, command=DDoS)
button_DDoS.pack()

Autorun_button = Button(root, image=autorun_image, borderwidth=0, command=Autorun)
Autorun_button.pack()

root.mainloop()
