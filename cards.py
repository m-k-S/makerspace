#!/usr/bin/env python

# -----------------------------------------------------------
# Functions for handling serial reading from smartcards (Columbia IDs)
# Written for the 2017 Columbia Makerspace swipe system
# - Max Aalto, Yonah Elorza 2017
# -----------------------------------------------------------

from cachetools import LRUCache
from smartcard.CardMonitoring import CardObserver
from smartcard.util import toHexString

class IDReader(CardObserver):
    def __init__(self):
        self.cache = LRUCache(maxsize=100)
        self.n = 1

    def update(self, observable, actions):
        (addedcards, removedcards) = actions
        for card in addedcards:
            self.cache[str(self.n)] = toHexString(card.atr)
            self.n += 1
