#!/usr/bin/env python

# -----------------------------------------------------------
# GUI tool for keeping track of users & the tools they are
# trained on in Columbia's student run Makerspace
# Written for the 2017 Columbia Makerspace swipe system
# - Max Aalto, Yonah Elorza 2017
#
# DISCLAIMER: We are fully aware this is vulnerable to SQL injection --
# PLEASE do not open a web interface for SQL queries for any reason
# -----------------------------------------------------------

from datetime import datetime
import sys
import Tkinter
from Tkinter import *
import ttk
from cards import *
from manage import *
import time

# Dependencies:
# - mysql 2.2 (mySQL Python connector)
# - pyscard 1.9.5 (Smartcard Reader)
#   * swig 3.0.12
#       ** PCRE
# - cachetools 2.0.0 (for memory caching)

import mysql.connector
from cachetools import LRUCache
from smartcard.CardMonitoring import CardMonitor, CardObserver
from smartcard.util import toHexString

# Establish connection to Makerspace MySQL database;
# This database should have the name 'makerspace',
# a table named 'users', and a table named 'logs'
#cnx = mysql.connector.connect(user='makerspace', password='',
#                               host='127.0.0.1',
#                               database='makerspace')

# Initialize ID monitor -- IDObserver is an instance of
# IDReader, defined in cards.py, which has a callable
# cache dictionary (IDReader.cache), the latest entry of
# which will be the last card read by the HID reader
IDMonitor = CardMonitor()
IDObserver = IDReader()
IDMonitor.addObserver(IDObserver)

def getData():
     return 0
def setData():
     return 0
def printa():
     print unlocked

#Main Window
window = Tkinter.Tk()
window.title("Card Swipe System")

#Variables for UI
uni = StringVar()
user = BooleanVar()
printer = BooleanVar()
laser = BooleanVar()
mill = BooleanVar()
vinyl = BooleanVar()
solder = BooleanVar()
drill = BooleanVar()
sewing = BooleanVar()
hand = BooleanVar()
osc = BooleanVar()
super = BooleanVar()
ban = BooleanVar()
unlocked = BooleanVar()
flag = 0

#Modding main window to make it tabbable
nb = ttk.Notebook(window)
swiper = ttk.Frame(nb)
superUserAuth = ttk.Frame(nb)
permissions = ttk.Frame(nb)

#Superuser Authentication Frame
authFrame = Frame(superUserAuth)
authFrame.pack(side = TOP, expand = 1, fill = "both")
T0 = Checkbutton(authFrame, text = "Unlock on Superuser Swipe", variable = unlocked, onvalue = 1, offvalue = 0, padx = 5, pady = 5)
T0.pack(side = TOP, expand = 1, fill = "both")

#permissions Frame
#Displays current UNI
permFrame1 = Frame(permissions)
permFrame2 = Frame(permissions)
permFrame3 = Frame(permissions)
permFrame1.pack(side = TOP, expand = 1, fill = "x")
permFrame2.pack(side = TOP, expand = 1, fill = "x")
permFrame3.pack(side = RIGHT, expand = 1, fill = "both")

#UNI Entry and Display
L1 = Label(permFrame1, text = "UNI")
E1 = Entry(permFrame1, text = uni)

L1.pack(side = LEFT, expand = 1, fill = "x")
E1.pack(side = LEFT, expand = 1, fill = "x")

#Get and Set Buttons
B1 = Button(permFrame1, text="Get", command = getData, padx = 5, pady = 5)
B2 = Button(permFrame2, text="Set", command = setData, padx = 5, pady = 5)    
B1.pack(side = RIGHT)
B2.pack(side = RIGHT)

#All the different tool trainings
T0 = Checkbutton(permFrame3, text = "User", variable = user, onvalue = 1, offvalue = 0, state = DISABLED, padx = 5, pady = 5)
T1 = Checkbutton(permFrame3, text = "3D Printer", variable = printer, onvalue = 1, offvalue = 0, state = DISABLED, padx = 5, pady = 5)
T2 = Checkbutton(permFrame3, text = "Laser Cutter", variable = laser, onvalue = 1, offvalue = 0, state = DISABLED, padx = 5, pady = 5)
T3 = Checkbutton(permFrame3, text = "CNC Mill", variable = mill, onvalue = 1, offvalue = 0, state = DISABLED, padx = 5, pady = 5)
T4 = Checkbutton(permFrame3, text = "Vinyl Cutter", variable = vinyl, onvalue = 1, offvalue = 0, state = DISABLED, padx = 5, pady = 5)
T5 = Checkbutton(permFrame3, text = "Soldering", variable = solder, onvalue = 1, offvalue = 0, state = DISABLED, padx = 5, pady = 5)
T6 = Checkbutton(permFrame3, text = "Drill Press", variable = drill, onvalue = 1, offvalue = 0, state = DISABLED, padx = 5, pady = 5)
T7 = Checkbutton(permFrame3, text = "Sewing Machine", variable = sewing, onvalue = 1, offvalue = 0, state = DISABLED, padx = 5, pady = 5)
T8 = Checkbutton(permFrame3, text = "Hand Tools", variable = hand, onvalue = 1, offvalue = 0, state = DISABLED, padx = 5, pady = 5)
T9 = Checkbutton(permFrame3, text = "Oscilloscope", variable = osc, onvalue = 1, offvalue = 0, state = DISABLED, padx = 5, pady = 5)
T10 = Checkbutton(permFrame3, text = "Superuser", variable = super, onvalue = 1, offvalue = 0, state = DISABLED, padx = 5, pady = 5)
T11 = Checkbutton(permFrame3, text = "Banned", variable = ban, onvalue = 1, offvalue = 0, state = DISABLED, padx = 5, pady = 5)

T0.grid(row = 1, column = 1, sticky = "W")
T1.grid(row = 2, column = 1, sticky = "W")
T2.grid(row = 3, column = 1, sticky = "W")
T3.grid(row = 4, column = 1, sticky = "W")
T4.grid(row = 5, column = 1, sticky = "W")
T5.grid(row = 6, column = 1, sticky = "W")
T6.grid(row = 1, column = 2, sticky = "W")
T7.grid(row = 2, column = 2, sticky = "W")
T8.grid(row = 3, column = 2, sticky = "W")
T9.grid(row = 4, column = 2, sticky = "W")
T10.grid(row = 5, column = 2, sticky = "W")
T11.grid(row = 6, column = 2, sticky = "W")

nb.add(swiper, text="Swiper")
nb.add(superUserAuth, text="Superuser Authentication")
nb.add(permissions, text="User Permissions")

nb.pack(expand=1, fill="both")

while True:
	window.update()
	if(unlocked.get() == 1):
		T0.config(state = NORMAL)
		T1.config(state = NORMAL)
		T2.config(state = NORMAL)
		T3.config(state = NORMAL)
		T4.config(state = NORMAL)
		T5.config(state = NORMAL)
		T6.config(state = NORMAL)
		T7.config(state = NORMAL)
		T8.config(state = NORMAL)
		T9.config(state = NORMAL)
		T10.config(state = NORMAL)
		T11.config(state = NORMAL)
		flag = 1
	if(unlocked.get() == 0) and (flag == 1):
		T0.config(state = DISABLED)
		T1.config(state = DISABLED)
		T2.config(state = DISABLED)
		T3.config(state = DISABLED)
		T4.config(state = DISABLED)
		T5.config(state = DISABLED)
		T6.config(state = DISABLED)
		T7.config(state = DISABLED)
		T8.config(state = DISABLED)
		T9.config(state = DISABLED)
		T10.config(state = DISABLED)
		T11.config(state = DISABLED) 
		flag = 0   

# On: SIGINT - cnx.close()
