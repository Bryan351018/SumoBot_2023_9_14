#!/usr/bin/env pybricks-micropython
"""EV3 brick, motor, and sensor objects needed for the program"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, InfraredSensor
from pybricks.parameters import Port, Direction

# The brick
brick = EV3Brick()
'''The brick'''

# Turntable motor
table = Motor(Port.C)
'''Turntable motor'''

# Infrared proximity sensor 1
infprox1 = InfraredSensor(Port.S1)
'''Infrared proximity sensor 1'''

# Infrared proximity sensor 2
infprox2 = InfraredSensor(Port.S4)
'''Infrared proximity sensor 2'''
