from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.ev3devices import UltrasonicSensor
from pybricks.tools import wait, StopWatch
from pybricks.ev3devices import GyroSensor
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
        self.boxsize = 70
        self.left_motor = Motor(Port.B)
        self.right_motor = Motor(Port.C)
        self.robot = DriveBase(self.left_motor, self.right_motor, wheel_diameter=55.5, axle_track=125)
        self.fork=Fork()
        self.gs=GyroSensor(Port.S3)
        self.gs.reset_angle(0)
        #self.mysensor = UltrasonicSensor(Port.S1)

    def moveforward(self, distanceinCm):
        self.robot.straight(distanceinCm)

    def tourn(self, degree):
        self.robot.turn((degree - self.gs.angle())-15)
        for x in range(10):
            self.robot.turn((degree-self.gs.angle())/2)


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
        self.robot.straight(self.timer.time * -100)

    def movetoWH(self):
        self.moveforward(self.boxsize * -2)
        self.tourn(180)
        self.moveforward(self.boxsize)


        
    def movetocord(self,x,y,jvb,color):
        self.movetoWH()
        self.moveforward(self.boxsize * y)
        if jvb == 1:  # True = jobra, False = balra
            self.tourn(90)
        else:
            self.tourn(270)
        self.fork.movetolevel(x)
        self.moveforward(self.boxsize * 3)
        if self.fork.colorcheck(color):
            return True
        return False

    def movebackfromcord(self,x,y):
        self.fork.lift()
        self.moveforward(self.boxsize*-3)
        self.tourn(0)
        self.moveforward(self.boxsize*(y+3))
        self.fork.lift()
    
    


