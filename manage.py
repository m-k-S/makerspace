#!/usr/bin/env python

# -----------------------------------------------------------
# Functions for modifying data in SQL databases
# Written for the 2017 Columbia Makerspace swipe system
# - Max Aalto, Yonah Elorza 2017
# -----------------------------------------------------------

from datetime import datetime
import sys

def add_user(uid, uni, lastname, firstname, dict):

    try:
	default_list = [uni, lastname, firstname, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	if(uni == 'ye2184'):
        	default_list = [uni, lastname, firstname, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
	dict[uid] = default_list
    except:
        e = sys.exc_info()[0]
        return e

def change_permissions(uid, field, perm, dict):

    try:
        current_list = dict[uid]
	if (field == user):
		current_list[3] = perm
	else if (field == drill):
		current_list[4] = perm
	else if (field == mill):
		current_list[5] = perm
	else if (field == sewing):
		current_list[6] = perm
	else if (field == printer):
		current_list[7] = perm
	else if (field == solder):
		current_list[8] = perm
	else if (field == oscope):
		current_list[9] = perm
	else if (field == vinyl):
		current_list[10] = perm
	else if (field == laser):
		current_list[11] = perm
	else if (field == super):
		current_list[12] = perm
	else if (field == banned):
		current_list[13] = perm
	dict[uid] = current_list
    except:
        e = sys.exc_info()[0]
        return e

#Not currently implemented
'''
def log_entry(uid, uni, cnx):

    try:
        cursor = cnx.cursor()
        LOG_ADD = ("INSERT INTO entries "
                  "(uid, uni, timestamp) "
                  "VALUES (%s, %s, %s)")

        LOG_DATA = (uid, uni, datetime.now().strftime("%A, %d %B %Y %I:%M%p"))

        res = cursor.execute(LOG_ADD, LOG_DATA)
        cnx.commit()
        cursor.close()
        return res
    except:
        e = sys.exc_info()[0]
        return e
'''

# Function for querying the credentials (if any exist) for
# a given swiped card
# To call this function:
#   Pass the UID of the card, the field to query, and the MySQL db connection
def query_card(uni, field, dict):

    try:
        current_list = dict[uid]
	if (field == user):
		return current_list[3]
	else if (field == drill):
		return current_list[4]
	else if (field == mill):
		return current_list[5]
	else if (field == sewing):
		return current_list[6]
	else if (field == printer):
		return current_list[7]
	else if (field == solder):
		return current_list[8]
	else if (field == oscope):
		return current_list[9]
	else if (field == vinyl):
		return current_list[10]
	else if (field == laser):
		return current_list[11]
	else if (field == super):
		return current_list[12]
	else if (field == banned):
		return current_list[13]
	dict[uid] = current_list
    except:
        e = sys.exc_info()[0]
        return e
