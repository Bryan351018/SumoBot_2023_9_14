#!/usr/bin/env pybricks-micropython
"""EV3 brick, motor, and sensor objects needed for the program"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor, ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
import math

# The brick
brick = EV3Brick()
'''The brick'''

# Left motor
Lmotor = Motor(Port.B, Direction.CLOCKWISE)
'''Left motor'''

# Right motor
Rmotor = Motor(Port.C, Direction.CLOCKWISE)
'''Right motor'''

# Wheel diameter
WHEEL_D = 43

# Track base
TRACK_B = 95

# Wheel circumference
whl_circ = 2 * WHEEL_D * math.pi

# Track circle circumference
trk_circ = 2 * TRACK_B * math.pi

# Drive base
base = DriveBase(Lmotor, Rmotor, WHEEL_D, TRACK_B)

# Infrared proximity sensor
infprox = InfraredSensor(Port.S2)
'''Infrared proximity sensor 1'''

# Left light sensor
L_light = ColorSensor(Port.S1)
'''Left light sensor'''

# Right light sensor
R_light = ColorSensor(Port.S4)
'''Right light sensor'''
