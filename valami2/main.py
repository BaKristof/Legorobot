#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.ev3devices import ColorSensor
from pybricks.tools import wait
from fork import Fork
#from move import Move
from warehouse import WH
import time


# Create your objects here

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize a motor at port B.
cs=ColorSensor(Port.S1)
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=125)
#fork_motor.run_angle(500,-650)
#robot.turn(-90)
#time.sleep(15)
#robot.turn(90)
#my_move = Move()
my_fork = Fork()
my_WH = WH()
robot.drive(100,10)
wait(1000)
robot.stop()
#my_fork.movetolevel(2)
#my_fork.lift()
#my_fork.lift()
#my_move.tourn90(True,True)
#forktolevel = Fork.movetolevel
#forklift = Fork.lift
#forktolevel(2)

kell=['K','K']

for x in kell:
    for y in my_WH.findbox(x):
        print("a kordináták "+str(y))

 

ev3.speaker.beep()


ev3.speaker.beep(frequency=1000, duration=500)

