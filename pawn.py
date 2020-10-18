class Pawn() :

    def __init__(self, color):
        self.color = color
        self.symbol = color[0]
    
    def __str__(self):
        return self.symbol

class Empty() :
    def __init__(self):
        self.symbol = "x"
    
    def __str__(self):
        return self.symbol

