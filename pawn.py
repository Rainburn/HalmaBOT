class Pile() :

    def __init__(self, row_initial, col_initial):
        self.row = row_initial
        self.col = col_initial

    def getRow(self) :
        return self.row
    
    def getCol(self) :
        return self.col
    
    def setRow(self, row) :
        self.row = row

    def setCol(self, col) :
        self.col = col

class Pawn(Pile) :

    def __init__(self, row_init, col_init, color):
        super().__init__(row_init, col_init)
        self.color = color
        self.symbol = color[0]

        if (self.symbol == "R") :
            self.curr_field = "RF"
            self.init_field = "RF"
        else :
            self.curr_field = "GF"
            self.init_field = "GF"
        # Status determines whether Pawn has left the house or already in target's house
        # RF = Red Field
        # FF = Free Field
        # GF = Green Field
    
    def __str__(self):
        return self.symbol

    def getCurrField(self) :
        return self.curr_field
    
    def getInitField(self) :
        return self.init_field

class Empty(Pile) :
    def __init__(self, row_init, col_init):
        super().__init__(row_init, col_init)
        self.symbol = "x"
    
    def __str__(self):
        return self.symbol
