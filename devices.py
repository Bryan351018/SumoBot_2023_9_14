#!/usr/bin/env pybricks-micropython
"""EV3 brick, motor, and sensor objects needed for the program"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor, ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

# The brick
brick = EV3Brick()
'''The brick'''

# Left motor
Lmotor = Motor(Port.B, Direction.CLOCKWISE)
'''Left motor'''

# Right motor
Rmotor = Motor(Port.C, Direction.CLOCKWISE)
'''Right motor'''

# Drive base
base = DriveBase(Lmotor, Rmotor, 43, 95)

# Infrared proximity sensor
infprox = InfraredSensor(Port.S2)
'''Infrared proximity sensor 1'''

# Left light sensor
L_light = ColorSensor(Port.S1)
'''Left light sensor'''

# Right light sensor
R_light = ColorSensor(Port.S4)
'''Right light sensor'''
