#!/usr/bin/env python

# -----------------------------------------------------------
# Functions for modifying data in SQL databases
# Written for the 2017 Columbia Makerspace swipe system
# - Max Aalto, Yonah Elorza 2017
# -----------------------------------------------------------

from datetime import datetime
import sys

# Function for adding users to the user database
# To call this function:
#    Pass data arguments [first four] and the MySQL db connection
#    Remember to close your db connection if necessary (cnx.close)
def add_user(uid, uni, lastname, firstname, cnx):

    try:
        cursor = cnx.cursor()
        USR_ADD = ("INSERT INTO users "
                  "(uid, uni, lastname, firstname, user, drill, mill, sewing, printer, solder, oscope, vinyl, laser, super, banned) "
                  "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

        USR_DATA = (uid, uni, lastname, firstname, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

        res = cursor.execute(USR_ADD, USR_DATA)
        cnx.commit()
        cursor.close()
        return res
    except:
        e = sys.exc_info()[0]
        return e

# Function for changing user permissions in the user database
# To call this function:
#   Pass data arguments and the MySQL db connection
#   Perm is 1 or 0 depending on whether it is being added or removed
#   Field names are described in the users table
def change_permissions(uid, field, perm, cnx):

    try:
        cursor = cnx.cursor()
        USR_UPDATE = ("""UPDATE users
                     SET %s=%s
                     WHERE uid=%s""")

        USR_DATA = (field, perm, uid)

        res = cursor.execute(USR_UPDATE, USR_DATA)
        cnx.commit()
        cursor.close()
        return res
    except:
        e = sys.exc_info()[0]
        return e

# Function for logging a user entry into the Makerspace
# To call this function:
#   Pass the UID of the card and the MySQL db connection
def log_entry(uid, cnx):

    try:
        cursor = cnx.cursor()
        LOG_ADD = ("INSERT INTO logs "
                  "(uid, timestamp) "
                  "VALUES (%s, %s)")

        LOG_DATA = (uid, datetime.now().strftime("%A, %d %B %Y %I:%M%p"))

        res = cursor.execute(LOG_ADD, LOG_DATA)
        cnx.commit()
        cursor.close()
        return res
    except:
        e = sys.exc_info()[0]
        return e

# Function for querying the credentials (if any exist) for
# a given swiped card
# To call this function:
#   Pass the UID of the card, the field to query, and the MySQL db connection
def query_card(uid, field, cnx):

    try:
        cursor = cnx.cursor()
        QUERY = ("""SELECT %s
                FROM users
                WHERE uid=%s""")

        QUERY_DATA = (field, uid)

        res = cursor.execute(QUERY, QUERY_DATA)
        cnx.commit()
        cursor.close()
        return res
    except:
        e = sys.exc_info()[0]
        return e    
