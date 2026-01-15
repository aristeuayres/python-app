#01 coding exercise.

#Write a simple function named get_hostname which returns the hostname of this server.


import socket

def get_hostname():

    return socket.hostname()

#02 coding exercise. 

#Create a function named get_date_dd_mm_yyyy which returns the current date in the following
format: DD-MM-YYYY

from datetime import datetime

def get_date_dd_mm_yyyy():
    
    return datetime.now(),strftime("%d-%m-%Y")
 