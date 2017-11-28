#!/usr/bin/python
# File:
# Description:

import time
import atexit
import Winder

rots_per_day = 750
rot_rate = 30
rot_type = "ALT"

winder = Winder(rots_per_day, rot_rate, rot_type)
while (winder.get_turn_count() < rots_per_day):
    winder.rotate_watch()
    time.sleep(winder.get_pause_interval())