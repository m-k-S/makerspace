#!/usr/bin/env python

# -----------------------------------------------------------
# User struct for DB handling
# - Max Aalto, Yonah Elorza 2017
# -----------------------------------------------------------

class MakerspaceUser:
    def __init__(self, uid, uni):
        self.uid = uid
        self.uni = uni
        self.permissions = {
            'banned': 0
            'user': 0
            'drill': 0
            'mill': 0
            'sewing': 0
            'printer': 0
            'soldering': 0
            'oscope': 0
            'vinyl': 0
            'laser': 0
            'super': 0
        }

    def change_perms(type, level):
        self.permissions[type] = level
