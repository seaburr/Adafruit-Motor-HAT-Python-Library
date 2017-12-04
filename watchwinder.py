#!/usr/bin/python
# File: watchwinder.py
# Description: Uses Winder class to wind watch at specified speed, rate, and direction.

import time
import atexit
from Winder import Winder

rots_per_day = 1000
rot_rate = 60
rot_type = "ALT"

winder = Winder(rots_per_day, rot_rate, rot_type)
while (winder.get_turn_count() < rots_per_day):
    winder.rotate_watch()
    print(winder.get_pause_interval())
    print(winder.get_turn_count())
    time.sleep(winder.get_pause_interval())
