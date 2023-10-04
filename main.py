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

# Base driving speed (mm/s)
BASE_SPEED = 100
'''Base driving speed'''

# Braking backward travel (mm), must be negative
BRAKE_TRAVEL = -50
'''Braking backward travel (mm), must be negative'''

# Table reflectivity threshold
EDGE_THRES = 20
'''Table reflectivity threshold'''

# # IR robot detection threshold (%)
# IR_PROX_THRES = 50
# '''IR robot detection threshold'''

# IR robot detection speed multiple
IR_SPD_MULT = 3
'''IR robot detection speed multiple'''

# IR proximity detection
def proxFunc():
    '''IR proximity detection'''
    while True:
        brick.screen.draw_text(0, 0, str(infprox.distance()))
        wait(T_EPS)
        brick.screen.clear()


# Drive cycle
def driveFunc():
    '''Drive cycle'''
    while True:
        # Go forward, with speed increasing as the robot gets closer
        base.drive(BASE_SPEED, 0)
        # Wait for table edge
        while L_light.reflection() > EDGE_THRES and R_light.reflection() > EDGE_THRES:
            wait(T_EPS)
        # Stop
        base.straight(BRAKE_TRAVEL)
        # Turn around
        base.turn(90)

# Start drive
Thread(target=driveFunc).start()

# Start proximity detection
Thread(target=proxFunc).start()

# Infinite pause to keep the program running
while True:
    wait(T_EPS)
