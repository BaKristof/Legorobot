from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.ev3devices import ColorSensor
from pybricks.parameters import Color
class Fork:
    fork = Motor(Port.A)
    liftdistanceCm = 1.5
    degreetoCm = 0.025
    levelinCm = 13
    level = 0
    islift = False 
    cs = ColorSensor(Port.S1)

    def colors(valami):
        szinek = {
            Color.BLACK:'B',
            Color.GREEN:'G',
            Color.YELLOW:'Y',
            Color.RED:'R',
            Color.WHITE:'W',
        }
        return szinek.get(valami,'X')

    def movetolevel(self, targetlevel):
        c = self.level - targetlevel
        self.fork.run_angle(100, ((c * self.levelinCm) / self.degreetoCm))
        self.level = targetlevel
        print("Move to level: " + str(targetlevel))

    def lift(self):
        if self.islift:
            self.fork.run_angle(100, self.liftdistanceCm / self.degreetoCm)
            self.islift = False
        else:
            self.fork.run_angle(-100, self.liftdistanceCm / self.degreetoCm)
            self.islift = True
            
    def colorcheck(self,color):
        if self.colors(self.cs.color()) == color:
            return True
        return False
    def getcolor(self):
       return self.colors(self.cs.color())      
