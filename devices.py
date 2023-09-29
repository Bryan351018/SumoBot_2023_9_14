#!/usr/bin/env pybricks-micropython
"""EV3 brick, motor, and sensor objects needed for the program"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor, ColorSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase

# The brick
brick = EV3Brick()
'''The brick'''

# Turntable motor
table = Motor(Port.A)
'''Turntable motor'''

# Left motor
Lmotor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
'''Left motor'''

# Right motor
Rmotor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
'''Right motor'''

# Drive base
base = DriveBase(Lmotor, Rmotor, 65, 225)

# Infrared proximity sensor 1
infprox1 = InfraredSensor(Port.S1)
'''Infrared proximity sensor 1'''

# Infrared proximity sensor 2
infprox2 = InfraredSensor(Port.S4)
'''Infrared proximity sensor 2'''

# Left light sensor
L_light = ColorSensor(Port.S3)
'''Left light sensor'''

# Right light sensor
R_light = ColorSensor(Port.S2)
'''Right light sensor'''
