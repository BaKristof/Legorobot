from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.ev3devices import UltrasonicSensor
from pybricks.tools import wait, StopWatch
from fork import Fork
import math
class Move:
    def __init__(self):
        self.degreetoCm = 0.025
        self.pi = math.pi
        self.wd = 55.5 
        self.timer = StopWatch()
        self.positionX = -1
        self.positionY = 0
        self.distenceBetweenBoxCm = 70
        self.left_motor = Motor(Port.B)
        self.right_motor = Motor(Port.C)
        self.robot = DriveBase(self.left_motor, self.right_motor, wheel_diameter=55.5, axle_track=125)
        self.fork=Fork()
        #self.mysensor = UltrasonicSensor(Port.S1)
        #self.myleftsensor = nxt.sensor.Port.S2
        #self.myrightsensor = nxt.sensor.Port.S3

    def moveforward(self, distanceinCm):
        self.robot.straight(100)

    def tourn(self, degree):
        self.robot.turn(degree)
        #a = (self.wd * self.pi) / 360
        #leftw = 0
       # rightw = 0
      #  speed = -150
      #  if lvr:
      #      leftw = (2.75 * 2 * self.pi) / 4
      #      rightw = (16 * 2 * self.pi) / 4
      #  else:
      #      leftw = (16 * 2 * self.pi) / 4
      #      rightw = (2.75 * 2 * self.pi) / 4
      #  if fvb:
       #     speed = speed * -1
       # self.left_motor.run_angle(speed, leftw / a)
        #self.right_motor.run_angle(speed, rightw / a)

    
    def movetobox(self):
        self.timer.reset()
        self.robot.drive(100,0)
        mehetmeg = True
        while mehetmeg:
            if self.mysensor.distance() <= 20:
                self.robot.stop()
                self.timer.pause()
                mehetmeg = False

    
    def backmovfrombox(self):
        self.robot.straight(timer.time*-100)

    def movetocord(self,x,y):
        tourn(180)
        moveforward((self.position-x)*self.distenceBetweenBoxCm)
        tourn(90) #lehet negatív ha rosz oldalon van a raktár
        self.fork.movetolevel(y)
        movetobox()
        self.fork.lift()
        backmovfrombox()
        self.fork.movetolevel(0)
        tourn(90) # ez is rosz lesz ha rosz oldalon van a raktár
        moveforward((self.position-x)*self.distenceBetweenBoxCm)
        self.fork.lift()
