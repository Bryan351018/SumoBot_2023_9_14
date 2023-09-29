#!/usr/bin/env pybricks-micropython
"""The program entry point"""

# Pybricks modules
from pybricks.tools import wait
# EV3 devices
from devices import *
# Native python modules
from threading import Thread

# Time epsilon, in ms (very small value)
T_EPS = 10
'''Time epsilon, in ms (very small value)'''

# Base driving speed
BASE_SPEED = 100
'''Base driving speed'''

# Braking backward travel (mm), must be negative
BRAKE_TRAVEL = -50
'''Braking backward travel (mm), must be negative'''

# Table turning speed (deg/s)
TABLE_SPEED = 100
'''Table turning speed (deg/s)'''

# Table turning angle (deg)
TABLE_ANG = 45
'''Table turning angle (deg)'''

# Table reflectivity threshold
EDGE_THRES = 20
'''Table reflectivity threshold'''

# Radar movement cycle
def moveRadarFunc():
    '''Radar movement cycle'''
    # Main turntable loop
    while True:
        table.run_target(TABLE_SPEED, TABLE_ANG)
        table.run_target(-TABLE_SPEED, -TABLE_ANG)

# Radar reading cycle
def readRadarFunc():
    # Clear screen
    brick.screen.clear()
    brick.screen.draw_text(0, 0, str(infprox1.distance()))
    brick.screen.draw_text(0, 15, str(infprox1.distance()))
    wait(500)

# Drive cycle
def driveFunc():
    '''Drive cycle'''
    while True:
        # Go forward
        base.drive(BASE_SPEED, 0)
        # Wait for table edge
        while L_light.reflection() > EDGE_THRES and R_light.reflection() > EDGE_THRES:
            wait(T_EPS)
        # Stop
        base.straight(BRAKE_TRAVEL)
        # Turn around
        base.turn(180)

# Start turntable
Thread(target=moveRadarFunc).start()

# Read turntable
# Thread(target=readRadarFunc).start()

# Start drive
Thread(target=driveFunc).start()

# Infinite pause to keep the program running
while True:
    wait(T_EPS)
