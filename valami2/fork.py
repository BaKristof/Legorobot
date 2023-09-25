from pybricks.ev3devices import Motor
from pybricks.parameters import Port

class Fork:
    fork = Motor(Port.A)
    liftdistanceCm = 1.5
    degreetoCm = 0.025
    levelinCm = 10.8
    level = 0
    islift = False 

    def movetolevel(self, targetlevel):
        c = self.level - targetlevel
        self.fork.run_angle(100, ((c * self.levelinCm) / self.degreetoCm))
        self.level = targetlevel
        print("Move to level: " + str(targetlevel))

    def lift(self):
        if self.islift:
            self.fork.run_angle(100, self.liftdistanceCm / self.degreetoCm)
            self.islift=False
        else:
            self.fork.run_angle(-100, self.liftdistanceCm / self.degreetoCm)
            self.islift=True
            

