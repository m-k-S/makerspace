#!/usr/bin/env python

# -----------------------------------------------------------
# GUI tool for keeping track of users & the tools they are
# trained on in Columbia's student run Makerspace
# Written for the 2017 Columbia Makerspace swipe system
# - Yonah Elorza 2017, with database assistance from Max Alto
# 
# -----------------------------------------------------------

from datetime import datetime
import sys
import Tkinter
from Tkinter import *
import ttk
from manage import *
import time
from pynput.keyboard import Key, Listener

# Dependencies:
#   * swig 3.0.12
#       ** PCRE

#Establish dictionary of users
dict = {}
'''
def on_press(key):
    swipe = 1

def on_release(key):
     var = 1

# Keyboard Listener
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
'''

#Swipe Data Get
def getData():
     uni.set(query_card(uid.get(),'uni',dict))
     user.set(query_card(uid.get(),'user',dict))
     printer.set(query_card(uid.get(),'printer',dict))
     laser.set(query_card(uid.get(),'laser',dict))
     mill.set(query_card(uid.get(),'mill',dict))
     vinyl.set(query_card(uid.get(),'vinyl',dict))
     solder.set(query_card(uid.get(),'solder',dict))
     drill.set(query_card(uid.get(),'drill',dict))
     sewing.set(query_card(uid.get(),'sewing',dict))
     osc.set(query_card(uid.get(),'oscope',dict))
     super.set(query_card(uid.get(),'super',dict))
     ban.set(query_card(uid.get(),'banned',dict))

def getDataUNI():
     uni.set(query_card(uni.get(),'uni',dict))
     user.set(query_card(uni.get(),'user',dict))
     printer.set(query_card(uni.get(),'printer',dict))
     laser.set(query_card(uni.get(),'laser',dict))
     mill.set(query_card(uni.get(),'mill',dict))
     vinyl.set(query_card(uni.get(),'vinyl',dict))
     solder.set(query_card(uni.get(),'solder',dict))
     drill.set(query_card(uni.get(),'drill',dict))
     sewing.set(query_card(uni.get(),'sewing',dict))
     osc.set(query_card(uni.get(),'oscope',dict))
     super.set(query_card(uni.get(),'super',dict))
     ban.set(query_card(uni.get(),'banned',dict))

def setDataUNI():
     change_permissions(uni.get(),'user',user.get(),dict)
     change_permissions(uni.get(),'printer',printer.get(),dict)
     change_permissions(uni.get(),'laser',laser.get(),dict)
     change_permissions(uni.get(),'mill',mill.get(),dict)
     change_permissions(uni.get(),'vinyl',vinyl.get(),dict)
     change_permissions(uni.get(),'solder',solder.get(),dict)
     change_permissions(uni.get(),'drill',drill.get(),dict)
     change_permissions(uni.get(),'sewing',sewing.get(),dict)
     change_permissions(uni.get(),'oscope',osc.get(),dict)
     change_permissions(uni.get(),'super',super.get(),dict)
     change_permissions(uni.get(),'banned',ban.get(),dict)
		

#Main Window
window = Tkinter.Tk()
window.title("Card Swipe System")

#Variables for UI
swipe = 0
uidT = StringVar()
uid = StringVar()
uni = StringVar()
firstname = StringVar()
lastname = StringVar()
user = StringVar()
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
signin = ttk.Frame(nb)
swiper = ttk.Frame(nb)
superUserAuth = ttk.Frame(nb)
permissions = ttk.Frame(nb)
signin.visible = False
swiper.visible = False
superUserAuth.visible = False
permissions.visible = False

#Sign-in frame
signFrame = Frame(signin)
signFrame.pack(side = TOP, expand = 1, fill = "both")
Z0 = Label(signFrame, text= "Tap to sign in")
Z0.pack(side = TOP, expand = 1, fill = "both")


#Adding Users
addFrame = Frame(swiper)
addFrame.pack(side = TOP, expand = 1, fill = "both")
B1 = Label(addFrame, text = "UID")
C1 = Entry(addFrame, textvariable = uidT)
B2 = Label(addFrame, text = "UNI")
C2 = Entry(addFrame, textvariable = uni)
B3 = Label(addFrame, text = "First Name")
C3 = Entry(addFrame, textvariable = firstname)
B4 = Label(addFrame, text = "Last Name")
C4 = Entry(addFrame, textvariable = lastname)
A0 = Button(addFrame, text = "Add User", command = add_user(uidT.get(),uni.get(),lastname.get(),firstname.get(),dict), padx = 5, pady = 5)
B1.pack(side = TOP, expand = 1, fill = "both")
C1.pack(side = TOP, expand = 1, fill = "both")
B2.pack(side = TOP, expand = 1, fill = "both")
C2.pack(side = TOP, expand = 1, fill = "both")
B3.pack(side = TOP, expand = 1, fill = "both")
C3.pack(side = TOP, expand = 1, fill = "both")
B4.pack(side = TOP, expand = 1, fill = "both")
C4.pack(side = TOP, expand = 1, fill = "both")
A0.pack(side = TOP, expand = 1, fill = "both")

#Superuser Authentication Frame
authFrame = Frame(superUserAuth)
authFrame.pack(side = TOP, expand = 1, fill = "both")
D0 = Checkbutton(authFrame, text = "Unlock on Superuser Swipe", variable = unlocked, onvalue = 1, offvalue = 0, padx = 5, pady = 5)
D0.pack(side = TOP, expand = 1, fill = "both")

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
B1 = Button(permFrame1, text="Get", command = getDataUNI, padx = 5, pady = 5)
B2 = Button(permFrame2, text="Set", command = setDataUNI, padx = 5, pady = 5, state = DISABLED)
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

nb.add(signin, text="Sign-In")
nb.add(swiper, text="Add User")
nb.add(superUserAuth, text="Superuser Authentication")
nb.add(permissions, text="User Permissions")

nb.pack(expand=1, fill="both")

while True:
	window.update()

	#Pulling current swiped user data
	if(swipe == 1) and ((signin.visible == True) or (permissions.visible == True)):
		permissions.visible = True
		uni.set(query_card(uid.get(),'uni',dict))
		user.set(query_card(uid.get(),'user',dict))
		printer.set(query_card(uid.get(),'printer',dict))
		laser.set(query_card(uid.get(),'laser',dict))
		mill.set(query_card(uid.get(),'mill',dict))
		vinyl.set(query_card(uid.get(),'vinyl',dict))
		solder.set(query_card(uid.get(),'solder',dict))
		drill.set(query_card(uid.get(),'drill',dict))
		sewing.set(query_card(uid.get(),'sewing',dict))
		osc.set(query_card(uid.get(),'oscope',dict))
		super.set(query_card(uid.get(),'super',dict))
		ban.set(query_card(uid.get(),'banned',dict))
		swipe = 0
	
	#Changing User Permissions
	if(superUserAuth.visible == True) and (swipe == 1) and (unlocked.get() == 1):
		super.set(query_card(uid.get(),'super',dict))
		if(super.get() == 1):
			permissions.visible = True
			B2.config(state = NORMAL)
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
	
	#Relocking user permissions		
	if(unlocked.get() == 0) and (flag == 1):
		B2.config(state = DISABLED)
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


