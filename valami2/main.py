#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.ev3devices import ColorSensor
from pybricks.tools import wait
from fork import Fork
from move import Move
from warehouse import WH
import time


# Create your objects here

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize a motor at port B.
#cs=ColorSensor(Port.S1)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=125)
#fork_motor.run_angle(500,-650)
#robot.straight(200)
#robot.turn(90)

#time.sleep(15)
#robot.turn(90)

my_move = Move()
my_fork = Fork()
my_WH = WH()
#my_fork.lift()
#robot.straight(-200)
#robot.turn(-180)
#robot.straight(100)
#robot.turn(90)
#robot.straight(200)
#my_fork.lift()

#print("a raktár méretei: "+str(my_WH.getlenghtofraktar())+" "+str(my_WH.gethightofraktar()))
#robot.drive(100,10)
#wait(1000)
#robot.stop()
#my_fork.movetolevel(1)
#my_fork.lift()
#my_fork.lift()
#my_move.tourn90(True,True)
#forktolevel = Fork.movetolevel
#forklift = Fork.lift
#forktolevel(2)
def bringbox():
    kell=['K','K']
    for x in kell:
        kordinates =my_WH.findbox(x)
        my_move.movetocord(kordinates[0],kordinates[1],kordinates[2],x)
        for y in my_WH.findbox(x):
            print("a kordináták "+str(y))

def checkallbox():
    for x in range(my_WH.getlenghtofrakta()):
        for y in range(my_WH.gethightofraktar()):
            my_WH.setboxcolor(1,x,y,my_fork.getcolor())
            
 

ev3.speaker.beep()


ev3.speaker.beep(frequency=1000, duration=500)

