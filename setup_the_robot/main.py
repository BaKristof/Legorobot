#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.ev3devices import Motor
from pybricks.ev3devices import GyroSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

#ev3.speaker.beep()
def tourn(self, degree):
    self.robot.turn((degree-self.gs.angle())-15)
    for x in range(10):
        self.robot.turn((degree-self.gs.angle())/2)

ev3 = EV3Brick()
boxsize= 70
leftm = Motor(Port.B)
rightm = Motor(Port.C)
robot = DriveBase(leftm,rightm,55.5,125)
gs=GyroSensor(Port.S3)
gs.reset_angle(0)
print( str(gs.angle()))

robot.straight(boxsize*-3)
robot.tourn(90)
robot.straight(boxsize*3)
wait(5000)
robot.straight(boxsize*-3)
robot.tourn(180)
robot.straight(boxsize*3)
wait(5000)
robot.straight(boxsize*-3)
robot.tourn(270)
robot.straight(boxsize*3)
robot.tourn(0)
robot.straight(boxsize*3)
wait(5000)
robot.straight(boxsize*-3)
robot.tourn(270)
robot.straight(boxsize*2)
robot.tourn(180)
robot.straight(boxsize*3)












