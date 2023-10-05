#!/usr/bin/env pybricks-micropython
"""The program entry point"""

# Pybricks modules
from pybricks.tools import wait, StopWatch
# EV3 devices
from devices import *
# Native python modules
from threading import Thread

# Time epsilon, in ms (very small value)
T_EPS = 10
'''Time epsilon, in ms (very small value)'''

# Base driving speed (mm/s)
BASE_SPEED = 30
'''Base driving speed'''

# Braking backward travel (mm), must be negative
BRAKE_TRAVEL = -50
'''Braking backward travel (mm), must be negative'''

# Table reflectivity threshold
EDGE_THRES = 33
'''Table reflectivity threshold'''

# IR robot detection speed multiple
IR_SPD_MULT = 3
'''IR robot detection speed multiple'''

# Get base drive speed from IR proximity
def spdFromProx(prox: int):
    pass
    '''Get base drive speed from IR proximity

    prox: current IR proximity reading (%)
    '''
    # return BASE_SPEED + BASE_SPEED * IR_SPD_MULT * ((100 - prox) / 100)
    

def angSpdFromProx(prox: int):
    # Base angular speed
    ang_spd = BASE_SPEED / whl_circ * 360
    # Final angular speed
    return ang_spd + ang_spd * IR_SPD_MULT * ((100 - prox) / 100)


# Run the base at a certain speed
def baseRun(spd: float):
    '''Run the base at a certain speed
    
    spd: linear speed (mm/s)
    '''

    # Angular speed
    ang_spd = spd / whl_circ * 360

    Lmotor.run(ang_spd)
    Rmotor.run(ang_spd)

# Run the base at a certain speed for a certainn distance
def baseDist(spd: float, dist: float):
    '''Run the base at a certain speed
    
    spd: linear speed (mm/s)
    '''

    # Angular speed
    ang_spd = spd / whl_circ * 360

    # Angular distance
    ang_dist = dist / whl_circ * 360

    Lmotor.run_angle(ang_spd, ang_dist, wait=False)
    Rmotor.run_angle(ang_spd, ang_dist)

# Turn the base a certain angle
def baseTurn(ang: float, ang_spd: float):
    '''Turn the base a certain angle
    
    ang: the angle to turn (deg)
    ang_speed: angular speed (deg/s)
    '''
    # Running distance
    dist = trk_circ * (ang / 360)

    # Angular distance
    ang_dist = dist / whl_circ * 360

    Lmotor.run_angle(-ang_spd, ang_dist, wait=False)
    Rmotor.run_angle(ang_spd, ang_dist)

# Brake the base
def baseBrake():
    '''Brake the base'''
    Lmotor.brake()
    Rmotor.brake()


def stopFunc():
    base.stop()

# Drive cycle
def driveFunc():
    '''Drive cycle'''

    # Create stopwatch
    watch = StopWatch()
    watch.resume()

    while True:
        # Wait for table edge
        while L_light.reflection() > EDGE_THRES and R_light.reflection() > EDGE_THRES:
            # Go forward, with speed increasing as the robot gets closer
            baseRun(angSpdFromProx(infprox.distance()))
            wait(T_EPS)
            
        # Stop
        # 1. Brake
        baseBrake()
        # 2. Reverse
        baseDist(BASE_SPEED * IR_SPD_MULT, BRAKE_TRAVEL)
        # Turn around
        baseTurn(90, 600)
 

# Start drive
Thread(target=driveFunc).start()

# Infinite pause to keep the program running
while True:
    wait(T_EPS)
