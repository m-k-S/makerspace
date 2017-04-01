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

from time import sleep
from cards import *
from manage import *

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
# a table named 'users', and a table named 'log'
cnx = mysql.connector.connect(user='makerspace', password='',
                               host='127.0.0.1',
                               database='makerspace')

# Initialize ID monitor -- IDObserver is an instance of
# IDReader, defined in cards.py, which has a callable
# cache dictionary (IDReader.cache), the latest entry of
# which will be the last card read by the HID reader
IDMonitor = CardMonitor()
IDObserver = IDReader()
IDMonitor.addObserver(IDObserver)


# if __name__ == '__main__':
    # Do something (pending UI development)
