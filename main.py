#!/usr/bin/env python

# -----------------------------------------------------------
# GUI tool for keeping track of users & the tools they are
# trained on in Columbia's student run Makerspaces
# - Max Aalto, Yonah Elorza 2017
# -----------------------------------------------------------

from time import sleep

# Dependencies:
# - mysql (mySQL Python connector)
# - pyscard (Smartcard Reader)
#   * swig
#       ** PCRE

import mysql.connector
from smartcard.CardMonitoring import CardMonitor, CardObserver
from smartcard.util import toHexString


class PrintObserver(CardObserver):
    
    def update(self, observable, actions):
        (addedcards, removedcards) = actions
        for card in addedcards:
            print("+Inserted: ", toHexString(card.atr))
        for card in removedcards:
            print("-Removed: ", toHexString(card.atr))

cardmonitor = CardMonitor()
cardobserver = PrintObserver()
cardmonitor.addObserver(cardobserver)
cardmonitor.deleteObserver(cardobserver)

# userDB = mysql.connector.connect(user='makerspace', password='',
#                                host='127.0.0.1',
#                                database='users')

# logDB = mysql.connector.connect(user='makerspace', password='',
                                # host='127.0.0.1',
                                # databae='log')

# if __name__ == '__main__':
