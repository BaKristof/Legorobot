class WH:
    def __init__(self):
        self.raktarB = [['X', 'X', 'X', 'X', 'X', 'X'], ['X', 'X', 'X', 'X', 'X', 'X']]
        self.raktarJ = [['X','X','X','X'],['X','X','X','X']]
    def findbox(self, color):
        print("itt is voltam")
        for x in range(2):
            for y in range(6):
                if self.raktarB[x][y] == color:
                    self.raktarB[x][y] = 'X'
                    return [x, y,1]
        for x in range(2):
            for y in range(4):
                if self.raktarJ[x][y] == color:
                    self.raktarJ[x][y] = 'X'
                    return [x, y,0]

    def setboxcolor(self,jvb,x,y,color):
        if jvb==1:
            self.raktarB[x][y]=color
        else:
            self.raktarJ[x][y]=color

    def getlenghtofraktar(self):
        return len(self.raktar[0])

    def gethightofraktar(self):
        return len(self.raktar)
