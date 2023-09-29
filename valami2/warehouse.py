class WH:
    def __init__(self):
        self.raktar = [['K', 'K', 'Z', 'K', 'Z', 'K'], ['Z', 'K', 'K', 'K', 'Z', 'Z']]

    def findbox(self, color):
        print("itt is voltam")
        for x in range(2):
            for y in range(6):
                if self.raktar[x][y] == color:
                    self.raktar[x][y] = 'X'
                    return [x, y]

    def detectbox(self):  # Added missing colon
        # Add your code for the detectbox method here

    def getlenghtofraktar(self):
        return len(self.raktar[0])

    def gethightofraktar(self):
        return len(self.raktar)
