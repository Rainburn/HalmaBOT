from pawn import Pile, Pawn, Empty

class Board :

    def __init__(self, size):
        self.size = size
        self.game_board = [[] for i in range(size)]

        for i in range(size):
            for j in range(size):
                if (i + j <= 3):
                    self.game_board[i].append(Pawn(i, j, "RED"))

                elif (2 * size - (i + j) <= 5):
                    self.game_board[i].append(Pawn(i, j, "GREEN"))
                
                else :
                    self.game_board[i].append(Empty(i, j))

    
    def swapPosition(self, row_initial, col_initial, row_final, col_final):
        pileInitial = self.game_board[row_initial][col_initial]
        pileFinal = self.game_board[row_final][col_final]

        pileInitial.setRow(row_final)
        pileInitial.setCol(col_final)
        
        pileFinal.setRow(row_initial)
        pileFinal.setCol(col_initial)

        self.game_board[row_final][col_final] = pileInitial
        self.game_board[row_initial][col_initial] = pileFinal

    def canMoveEast(self, row_initial, col_initial, multiplier = 1) :
        row_shift = 0 * multiplier
        col_shift = 1 * multiplier 

        row_final = row_initial + row_shift
        col_final = col_initial + col_shift
        if (row_final >= self.size) or (col_final >= self.size) :
            return False
        
        pile = self.getPile(row_final, col_final)

        if (str(pile) == "x") :
            return True
        
        else :
            return False

    def canMoveSouthEast(self, row_initial, col_initial, multiplier = 1) :
        row_shift = 1 * multiplier
        col_shift = 1 * multiplier 

        row_final = row_initial + row_shift
        col_final = col_initial + col_shift
        if (row_final >= self.size) or (col_final >= self.size) :
            return False
        
        pile = self.getPile(row_final, col_final)

        if (str(pile) == "x") :
            return True
        
        else :
            return False

    def canMoveSouth(self, row_initial, col_initial, multiplier = 1) :
        row_shift = 1 * multiplier
        col_shift = 0 * multiplier 

        row_final = row_initial + row_shift
        col_final = col_initial + col_shift
        if (row_final >= self.size) or (col_final >= self.size) :
            return False
        
        pile = self.getPile(row_final, col_final)

        if (str(pile) == "x") :
            return True
        
        else :
            return False
    
    def canMoveSouthWest(self, row_initial, col_initial, multiplier = 1) :
        row_shift = 1 * multiplier
        col_shift = -1 * multiplier 

        row_final = row_initial + row_shift
        col_final = col_initial + col_shift
        if (row_final >= self.size) or (col_final >= self.size) :
            return False
        
        pile = self.getPile(row_final, col_final)

        if (str(pile) == "x") :
            return True
        
        else :
            return False

    def canMoveWest(self, row_initial, col_initial, multiplier = 1) :
        row_shift = 0 * multiplier
        col_shift = -1 * multiplier 

        row_final = row_initial + row_shift
        col_final = col_initial + col_shift
        if (row_final >= self.size) or (col_final >= self.size) :
            return False
        
        pile = self.getPile(row_final, col_final)

        if (str(pile) == "x") :
            return True
        
        else :
            return False
    
    def canMoveNorthWest(self, row_initial, col_initial, multiplier = 1) :
        row_shift = -1 * multiplier
        col_shift = -1 * multiplier 

        row_final = row_initial + row_shift
        col_final = col_initial + col_shift
        if (row_final >= self.size) or (col_final >= self.size) :
            return False
        
        pile = self.getPile(row_final, col_final)

        if (str(pile) == "x") :
            return True
        
        else :
            return False

    def canMoveNorth(self, row_initial, col_initial, multiplier = 1) :
        row_shift = -1 * multiplier
        col_shift = 0 * multiplier 

        row_final = row_initial + row_shift
        col_final = col_initial + col_shift
        if (row_final >= self.size) or (col_final >= self.size) :
            return False
        
        pile = self.getPile(row_final, col_final)

        if (str(pile) == "x") :
            return True
        
        else :
            return False

    def canMoveNorthEast(self, row_initial, col_initial, multiplier = 1) :
        row_shift = -1 * multiplier
        col_shift = 1 * multiplier 

        row_final = row_initial + row_shift
        col_final = col_initial + col_shift
        if (row_final >= self.size) or (col_final >= self.size) :
            return False
        
        pile = self.getPile(row_final, col_final)

        if (str(pile) == "x") :
            return True
        
        else :
            return False
    

    def takeEastPile(self, row_initial, col_initial, multiplier = 1) :
        row_shift = 0 * multiplier
        col_shift = 1 * multiplier 

        row_final = row_initial + row_shift
        col_final = col_initial + col_shift
        return self.getPile(row_final, col_final)

    def takeSouthEastPile(self, row_initial, col_initial, multiplier = 1) :
        row_shift = 1 * multiplier
        col_shift = 1 * multiplier 

        row_final = row_initial + row_shift
        col_final = col_initial + col_shift
        return self.getPile(row_final, col_final)

    def takeSouthPile(self, row_initial, col_initial, multiplier = 1) :
        row_shift = 1 * multiplier
        col_shift = 0 * multiplier 

        row_final = row_initial + row_shift
        col_final = col_initial + col_shift
        return self.getPile(row_final, col_final)
    
    def takeSouthWestPile(self, row_initial, col_initial, multiplier = 1) :
        row_shift = 1 * multiplier
        col_shift = -1 * multiplier 

        row_final = row_initial + row_shift
        col_final = col_initial + col_shift
        return self.getPile(row_final, col_final)

    def takeWestPile(self, row_initial, col_initial, multiplier = 1) :
        row_shift = 0 * multiplier
        col_shift = -1 * multiplier 

        row_final = row_initial + row_shift
        col_final = col_initial + col_shift
        return self.getPile(row_final, col_final)
    
    def takeNorthWestPile(self, row_initial, col_initial, multiplier = 1) :
        row_shift = -1 * multiplier
        col_shift = -1 * multiplier 

        row_final = row_initial + row_shift
        col_final = col_initial + col_shift
        return self.getPile(row_final, col_final)

    def takeNorthPile(self, row_initial, col_initial, multiplier = 1) :
        row_shift = -1 * multiplier
        col_shift = 0 * multiplier 

        row_final = row_initial + row_shift
        col_final = col_initial + col_shift
        return self.getPile(row_final, col_final)

    def takeNorthEastPile(self, row_initial, col_initial, multiplier = 1) :
        row_shift = -1 * multiplier
        col_shift = 1 * multiplier 

        row_final = row_initial + row_shift
        col_final = col_initial + col_shift
        return self.getPile(row_final, col_final)


    def getPile(self, row, col):
        return self.game_board[row][col]
        

    def printBoard(self):

        print()

        for i in range(self.size + 1):
            for j in range(self.size + 1):


                if (i == 0) and (j == 0) :
                    print("x", end="  ")
                
                elif (i == 0) :
                    if(j>10):
                        print(j-1, end=" ")
                    else:
                        print(j-1, end="  ")

                elif (j == 0) :
                    if(i <= 10):
                        print(i-1, end="  ")
                    else:
                        print(i-1, end=" ")

                else :
                    print(self.game_board[i-1][j-1], end="  ")
            
            print()

        print()
            


    def getSize(self):
        return self.size


