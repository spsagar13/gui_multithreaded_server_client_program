#!/usr/bin/env python3
############################################################
# Name      : Sagar Surendran
# UTA ID    : 1001448700
# Date      : 07-12-2020
# Brief     : Client implementation of the multi threaded
#             server client program
############################################################

from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter
from itertools import count
import time

# Flag for counter
val_ = 0

# Function to handle messagaes from the server
def receive():
    global val_
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
            if '-' in msg:
                txt = msg.split('-')[0]
                val_ = int(msg.split('-')[1])
                if txt == "pause":
                    print("value :", val_)
                    start_counter()
        except OSError:  # Possibly something went wrong.
            break

# Function to send the mssage ( {quit} ) to server 
def send(event=None):  # event is passed by binders.
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()

# Function to initate the counter 
def start_counter():
    global val_
    for i in range(val_, -1, -1):
        if val_ == 0:
            label.config(text="")
            return 
        label.config(text=str(i))
        time.sleep(1)
    msg_list.insert(tkinter.END, "Timer Expired. Waiting for Pause command from server.")
    label.config(text="")
    val_ = 0

# Function to clear the counter if it is running
def clear_counter():
    global val_ 
    if val_ == 0:
        msg_list.insert(tkinter.END, "No counter is running. Waiting for Pause command from server.")
    else:
        msg_list.insert(tkinter.END, "Counter stopped. Waiting for Pause command from server.")
        val_ = 0

# Function called to send the quit message during the closure of client through closing the window
def on_closing(event=None):
    my_msg.set("{quit}")
    send()


# TKinker implementation
top = tkinter.Tk()
top.title("Client")

messages_frame = tkinter.Frame(top)
# To send name and {quit} command through GUI
my_msg = tkinter.StringVar()  
my_msg.set("")
scrollbar = tkinter.Scrollbar(messages_frame)  
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=80, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()
button = tkinter.Button(top, text='Stop Counter', width=30, command=clear_counter)
button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)

label = tkinter.Label(top, fg="red")
label.pack()

# sockets implementation
HOST="127.0.0.1"
PORT=33000
BUFSIZ = 1024
ADDR = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(ADDR)

receive_thread = Thread(target=receive)
receive_thread.daemon = True
receive_thread.start()
receive_thread.join(1)

# Starting GUI
tkinter.mainloop()  
