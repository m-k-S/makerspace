api:

/equipment?tool=<toolname>
 - tool is optional.
 - if tool defined:
   --> {"toolname": {"in_use": True}}
 - otherwise:
   --> {"tool1": {"in_use": True}, "tool2": {"in_use": False}}

/is_open
  -->  {"open_until": "YYYYMMDD HH:MM:SS",
        "is_open": True}
