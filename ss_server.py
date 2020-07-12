#!/usr/bin/env python3
#########################################################
# Name      : Sagar Surendran
# UTA ID    : 1001348700
# Date      : 07/12/2020
# Brief     : Server implementaion of multi threaded 
#             server client program with simple GUI
#########################################################

from datetime import datetime
import socket
import threading
import tkinter as tk
import random
import time

root = tk.Tk()
root.title("Server")

#Place to show the commands/texts
text = tk.Text(master=root)
text.pack(expand=True, fill="both")

#Creting the start and stop buttons
frame = tk.Frame(master=root)
frame.pack()
b1 = tk.Button(master=frame, text="Start Server") 
b1.pack(side="left")
b2 = tk.Button(master=frame, text="Stop Server") 
b2.pack(side="left")

#Server Class
class Server:

    # Dictionaries to store clients, its names and addresses
    clients = {}
    addresses = {}
    # Universal flag to check if the server is already processing a client
    processing_client = False

    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Function to start listening to incoming connections
    def start_server(self):
        text.insert("insert","Listening for incoming connections..\n")
        self.s.bind(("",  33000))
        self.s.listen(5)
        self.condition()

   # Function to handle a client request, name checks
   # Note : Client with same name (despite upper or lower case) will not be allowed by the program
    def accept(self):
        c, addr = self.s.accept()
        c.send(bytes("Type your name and press enter!", "utf8"))
        self.addresses[c] = addr

        while True:
            name = c.recv(1024).decode("utf8")
            welcome = 'Welcome %s! If you ever want to quit, type {quit} and press enter to exit.' % name
            c.send(bytes(welcome, "utf8"))
            flag = False
            for key, value in self.clients.items():
                if value.lower() == name.lower():
                    flag = True
                    rename = '[ERROR] The name %s is already in use. Please provide a different name!' % name
                    c.send(bytes(rename, "utf8"))

            if not flag:
                break

        msg = "%s has been connected!" % name
        self.clients[c] = name
        text.insert("insert", "{} connected.\n".format(name))
    
    # Function to handle the incoming {quit} message from the client
    # It also sends the pause requests to clients
    def receive(self):

        # Remove clients from the dictionary when the client disconnects
        def e():
            for sock in list(self.clients):
                msg_ = sock.recv(1024)
                if msg_ == bytes("{quit}", "utf8"):
                    name = self.clients[sock]
                    sock.send(bytes("{quit}", "utf8"))
                    text.insert("insert", "Client {} has been disconnected.\n".format(name))
                    sock.close()
                    del self.clients[sock]
        # Periodically, in each 10 seconds, a random client is selected and a random pause in seconds between 3 and 9 
        # is selected and sent to that respectieve client
        def f():
            if self.clients and not self.processing_client:
                self.processing_client = True
                #the server should randomly select a connected client, then
                try:
                    c, name = random.choice(list(self.clients.items()))
                    num = random.randint(3,9)
                    msg = "pause-" + str(num)
                    
                    text.insert("insert", "sending {} to {}\n".format(msg,name))
                    c.send(bytes(msg, "utf8"))
                    time.sleep(10)
                    self.processing_client = False 
                except BrokenPipeError:
                    text.insert("insert", "Client has been disconnected.\n")
                
        t1_2_1 = threading.Thread(target=f)
        t1_2_1.daemon = True
        t1_2_1.start()
        t1_2_1.join(1)
        t1_2_2 = threading.Thread(target=e)
        t1_2_2.daemon = True
        t1_2_2.start()
        t1_2_2.join(1)

    # Function to handle accept and receive functions in thread
    def condition(self):
        while True:
            t1_1 = threading.Thread(target=self.accept)
            t1_1.daemon = True
            t1_1.start()
            t1_1.join(1)
            t1_2 = threading.Thread(target=self.receive)
            t1_2.daemon = True
            t1_2.start()
            t1_2.join(1)

# Initializing the server class
s1 = Server()

# Function called to start the server when the button is clicked
def start_server():
    t1 = threading.Thread(target=s1.start_server)
    t1.daemon = True
    t1.start()

# Function called to stop the server when the button is clicked
def destroy():
    root.destroy()
    exit(1)

# Main class
if __name__ == "__main__":
    b1.configure(command=start_server)
    b2.configure(command=destroy)
    t0 = threading.Thread(target=root.mainloop)
    t0.run()
