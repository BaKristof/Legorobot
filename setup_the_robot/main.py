#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.ev3devices import Motor
from pybricks.ev3devices import GyroSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase


ev3 = EV3Brick()
leftm = Motor(Port.B)
rightm = Motor(Port.C)
robot = DriveBase(leftm,rightm,55.5,125)
gs=GyroSensor(Port.S3)
gs.reset_angle(0)
robot.turn(80)
while gs.angle != 90:
    robot.turn((90-gs.angle())/2)


print( str(gs.angle()))

#ev3.speaker.beep()


