#!/usr/bin/env python

# -----------------------------------------------------------
# Functions for modifying data in SQL databases
# Written for the 2017 Columbia Makerspace swipe system
# - Max Aalto, Yonah Elorza 2017
# -----------------------------------------------------------

# Function for adding users to the user database
# To call this function in code:
#    Pass data arguments [first four] and the MySQL db connection
#    Remember to close your db connection if necessary (cnx.close)
def add_user(uid, uni, lastname, firstname, cnx):

    cursor = cnx.cursor()
    USR_ADD = ("INSERT INTO users "
              "(uid, uni, lastname, firstname) "
              "VALUES (%s, %s, %s, %s)")

    USR_DATA = (uid, uni, lastname, firstname)

    cursor.execute(USR_ADD, USR_DATA)
    cnx.commit()
    cursor.close()

# Function for changing user permissions in the user database
# To call this function in code:
#   Pass data arguments and the MySQL db connection
#   Perm is 1 or 0 depending on whether it is being added or removed
#   Field names are described in the users table
def change_permissions(uid, field, perm, cnx):

    cursor = cnx.cursor()
    USR_UPDATE = ("""UPDATE users
                 SET %s=%s
                 WHERE uid=%s""")

    USR_DATA = (field, perm, uid)

    cursor.execute(USR_UPDATE, USR_DATA)
    cnx.commit()
    cursor.close()
