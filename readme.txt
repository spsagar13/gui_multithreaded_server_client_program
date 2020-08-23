# Name   : Sagar Surendran
# UTA ID : 1001438700
# Brief  : Readme file for multi threaded server client program in GUI

#####################################################################################################################
# The multi threaded server program has been inspired from the server.py from the below source
# https://stackoverflow.com/questions/49742217/python-socket-threading-tkinter-how-to-know-the-message-sender
# The client program has been inspired from the below chat app implementaion
# https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170
#####################################################################################################################

Prerequisites
-------------
	Linux based machine/MacOS
	Python 3.x

	Below packages
	  datetime
	  socket
	  threading
	  tkinter
	  random
	  time
	  itertools

Sanity checks
-------------
   After unzipping it, you will see the below files.
   1. ss_server.py  - md5 0d09199da65fc853b3f5be95bb596d7e
   2. ss_client.py  - md5 234e06029823c759c11998c6e5f13f72 
   3. readme.txt    

Execution steps: 
---------------
 chmod 777 ss_server.py
 chmod 777 ss_client.py

Steps:
......
4 Terminals should be opened, for Server and 3 Clients

In terminal 1
  1. Type ./ss_server.py # GUI for the server will be opened
  2. click on the "Start Server" button
In terminal 2
  3. Type ./ss_client.py # GUI for the client 1 will be opened
  4. Type a required name and press enter
In terminal 3
  5. Type ./ss_client.py # GUI for the client 2 will be opened
  6. Type a required name and press enter
In terminal 4
  7. Type ./ss_client.py # GUI for the client 3 will be opened
  8. Type a required name and press enter

................................................................................................
-> To verify the duplicate name check, the same name can be given when creating the client name
ASSUMPTION : upper case/lower case versions of the same name is considerd equivalent 
-> To stop the counter, in any Client GUI, "Stop counter" button can be pressed.
   If the counter is running, it will stop the counter. If the counter is not running, it will
   display the appropriate message
-> To exit the client, either close the GUI window, or type "{quit}" and press enter
-> To exit server, either close the GUI or press "Stop Server" button
................................................................................................

NOTE : When exiting the client, it is observed that sometime, there is a delay in displying the connection abort message at the server side.
