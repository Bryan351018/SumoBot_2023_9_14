#!/usr/bin/env pybricks-micropython
"""The program entry point"""

# from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
#                                  InfraredSensor, UltrasonicSensor, GyroSensor)
# from pybricks.parameters import Port, Stop, Direction, Button, Color
# from pybricks.tools import wait, StopWatch, DataLog
# from pybricks.robotics import DriveBase
# from pybricks.media.ev3dev import SoundFile, ImageFile

# Pybricks mmodules
# from pybricks.tools import wait
# EV3 devices
from devices import *
# Native python modules
from os.path import exists

# Log group
log_group = "A"
# Log number
log_num = 1
# while exists("./robot_logs/" + log_group + str(log_num) + ".log"):
#     log_num += 1
#     if (log_num > 1000):
#         raise RuntimeError("Log number exceeded 1000. Please use a new log group.") 

# print("./robot_logs/" + log_group + str(log_num) + ".txt")
# Log file
# logfile = open("./robot_logs/" + log_group + str(log_num) + ".txt", "w+")
'''Log file'''

# logfile.write("Robot started")

# Table turning speed (deg/s)
table_speed = 300
# Table turning angle (deg)
table_ang = 120
# Table turning peiod
# table_T = table_ang / table_speed * 1000
# print(table_T)

# Main loop
while True:
    table.run_target(table_speed, table_ang)
    table.run_target(-table_speed, table_ang)

# Close log file
# logfile.close()
