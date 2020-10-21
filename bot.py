from board import Board
from player import *
from pawn import *

class Bot(Player):

    def __init__(self, color, board):
        super().__init__(color)
        self.board = board

    def __str__(self):
        return "BOT"

    def checkwin(self, color):
        win = True
        if (color == "R"):
            for i in range(4) :
                for j in range(4 - i) :
                    row = self.board.getSize() - (i + 1)
                    col = self.board.getSize() - (j + 1)

                    pile = self.board.getPile(row, col)
                    if (str(pile) == "x") or (str(pile) == "G") :
                        win = False
        elif (color == "G"):
            for i in range(4) :
                for j in range(4 - i) :
                    pile = self.board.getPile(i, j)
                    if (str(pile) == "x") or (str(pile) == "R") :
                        win = False
        return win


    def objFunc(self, color):
        valueR = 0
        valueG = 0
        n = self.board.getSize()
        now = None
        opponent = ""

        if (color == "R"):
            opponent = "G"
        elif (color == "G"):
            opponent = "R"

        win = self.checkwin(color)
        lose = self.checkwin(opponent)

        if win:
            value = 99999
        elif lose:
            value = -99999
        else:
            for i in range(n):
                for j in range (n):
                    now = self.board.getPile(i, j)
                    if str(now) == "R":
                        valueR += i + j
                    elif str(now) == "G":
                        valueG += (2*n + 2 - (i + j))
                    else:
                        continue
            
            if (color == "R"):
                value = valueR - valueG
            elif (color == "G"):
                value = valueG - valueR

        return value

    def minimax(self, depth, color, max = True, a = float("-inf"), b = float("inf")):
        #basis
        if (depth == 0) or (self.checkwin("R")) or (self.checkwin("G")):
            return self.objFunc(color), None
        
        #variabel dan move
        best_move = None

        moves = self.nextMove(color)
        # print(moves)

        if max:
            best_val = float("-inf")
        else:
            best_val = float("inf")
                
        #rekurens
        for i in range(len(moves)):
            #move: pindahin pion 
            initial_row = moves[i][0].getRow()
            initial_col = moves[i][0].getCol()   
            final_row = moves[i][1].getRow()
            final_col = moves[i][1].getCol()
            self.board.swapPosition(initial_row, initial_col, final_row, final_col)

            #panggil rekursif
            val, selected_move = self.minimax(depth-1, color, not max, a, b)
                
            #undo movenya
            self.board.swapPosition(final_row, final_col, initial_row, initial_col)

            if max and (val > best_val):
                best_val = val
                best_move = moves[i]
                a = max(a, val)
            if not max and (val < best_val):
                best_val = val
                best_move = moves[i]
                b = min(b, val)

            # pruning
            if (b <= a):
               return best_val, best_move

        return best_val, best_move


    def nextMove(self, color):
        moves = []
        for row in range(self.board.getSize()):
            for col in range(self.board.getSize()):

                currPile = self.board.getPile(row, col)
                # print(str(currPile))
                if str(currPile) != color:
                    continue
                
                # move = []
                # move.append(currPile) # From Pile
                # move.append(self.availablePos(currPile, color)) # Destination Pile
                # moves.append(move)
                temp = self.availablePos(currPile, color)
                for x in temp:
                    move = []
                    move.append(currPile)
                    move.append(x)
                    moves.append(move)
        
        return moves

    def availablePos(self, selected_pawn, color, moves=None, adj=True) :
                                                
        row_init = selected_pawn.getRow()
        col_init = selected_pawn.getCol()

        if moves is None:
            moves = []
        
        validPile = ["FF", "RF", "GF"]
        if str(selected_pawn) != color:
            validPile.remove(selected_pawn.getCurrField())
            # print("TESS")
        if selected_pawn.getCurrField() != "FF" and str(selected_pawn) != color:
            validPile.remove("FF")  # Moving out of the enemy's goal
        # print("INI VALID PILE ", validPile)

    

        for rowDelta in range(-1,2):
            for colDelta in range(-1,2):

                newRow = row_init + rowDelta
                newCol = col_init + colDelta

                if ((newRow == row_init and newCol == col_init) or
                    newRow < 0 or newCol < 0 or
                    newRow >= self.board.getSize() or newCol >= self.board.getSize()):
                    continue

                # Kasus keluar atau masuk dari daerah goal
                newPile = self.board.getPile(newRow, newCol)

                if str(newPile) == "x" :
                    continue

                if newPile.getCurrField() not in validPile:
                    continue

                if newPile.getCurrField() == "FF":
                    if adj: 
                        moves.append(newPile)
                    continue


                # Check jump pile

                newRow = newRow + rowDelta
                newCol = newCol + colDelta

                # Skip invalid values
                if (newRow < 0 or newCol < 0 or
                    newRow >= self.board.getSize() or newCol >= self.board.getSize()):
                    continue

                # Handle returning moves and moves out of/in to goals
                newPile = self.board.getPile(newRow, newCol)

                if str(newPile) == "x" :
                    continue

                if newPile in moves or (newPile.getCurrField() not in validPile):
                    continue

                if newPile.getCurrField() == "FF":
                    moves.insert(0, newPile)  
                    self.availablePos(newPile, color, moves, False)

        return moves 
        
    def updateBoard(self, board):
        self.board = board
