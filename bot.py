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
        now = Pawn.Empty()
        opponent = ""

        if (color == "R"):
            opponent = "G"
        elif (color == "G"):
            opponent = "R"

        win = self.checkwin(color, self.board)
        lose = self.checkwin(opponent, self.board)

        if win:
            value = 99999
        elif lose:
            value = -99999
        else:
            for i in range(n):
                for j in range (n):
                    now = self.board.getPile(i, j)
                    if Pawn.str(now) == "R":
                        valueR += i + j
                    elif Pawn.str(now) == "G":
                        valueG += (2*n + 2 - (i + j))
                    else:
                        continue
            
            if (color == "R"):
                value = valueR - valueG
            elif (color == "G"):
                value = valueG - valueR

        return value

    def minimax(self, depth, color, max = True, a = float("-inf"), b = float("inf")):
        #variabel dan move
        moves = self.nextMove(color)
        best_move = None
        if max:
            best_val = float("-inf")
        else:
            best_val = float("inf")

        #basis
        if (depth == 3) or (self.checkwin("R")) or (self.checkwin("G")):
            return self.objFunc(color, self.board), best_move

        #rekurens
        for i in range(len(moves)):
            #move: pindahin pion 
            initial_row = moves[i][0].getRow()
            initial_col = moves[i][0].getCol()   
            final_row = moves[i][1].getRow()
            final_col = moves[i][1].getCol()
            self.board.swapPosition(initial_row, initial_col, final_row, final_col)

            #panggil rekursif
            val, selected_move = self.minimax(depth+1, color, not max, a, b)
                
            #undo movenya
            self.board.swapPosition(final_row, final_col, initial_row, initial_col)

            if max and (val > best_val):
                best_val = val
                best_move = selected_move
                a = max(a, val)
            if not max and (val < best_val):
                best_val = val
                best_move = selected_move
                b = min(b, val)

            if (b <= a):
                return best_val, best_move

        return best_val, best_move

        # if depth == 0 or checkwin == True:
        #     return self.objFunc

        # if maxing:
        #     best_val = float("-inf")
        #     moves = self.get_next_moves(isMaxingColor)
        # else:
        #     best_val = float("inf")
        #     moves = self.get_next_moves((Tile.P_RED
        #             if isMaxingColor == Tile.P_GREEN else Tile.P_GREEN))

    def nextMove(self, color):
        moves = []
        for row in range(self.board.getSize()):
            for col in range(self.board.getSize()):

                currPile = self.board.getPile(row, col)

                if currPile != color:
                    continue
                
                move = []
                move[0] = currPile # From Pile
                move[1] = self.availablePos(currPile, color) # Destination Pile

                moves.append(move)
        
        return moves

    def availablePos(self, selected_pawn, color, moves=None, adj=True) :

        row_init = selected_pawn.getRow()
        col_init = selected_pawn.getCol()

        if moves is None:
            moves = []
        
        validPile = ["FF", "RF", "GF"]
        if selected_pawn.getCol != color:
            validPile.remove(selected_pawn.getCurrField)
        if selected_pawn.getCurrField != "FF" and selected_pawn.getCol != color:
            validPile.remove("FF")  # Moving out of the enemy's goal

        

        for rowDelta in range(-1,2):
            for colDelta in range(-1,2):

                newRow = row_init + rowDelta
                newCol = col_init + colDelta

                if ((newRow == row_init and newCol == col_init) or
                    newRow < 0 or newCol < 0 or
                    newRow >= self.b_size or newCol >= self.b_size):
                    continue

                # Handle moves out of/in to goals
                newPile = self.board[newRow][newCol]
                if newPile.tile not in validPile:
                    continue

                if newPile.getCurrField == "FF":
                    if adj:  # Don't consider adjacent on subsequent calls
                        moves.append(newPile)
                    continue

                # Check jump tiles

                newRow = newRow + rowDelta
                newCol = newCol + colDelta

                # Skip checking degenerate values
                if (newRow < 0 or newCol < 0 or
                    newRow >= self.b_size or newCol >= self.b_size):
                    continue

                # Handle returning moves and moves out of/in to goals
                newPile = self.board[newRow][newCol]
                if newPile in moves or (newPile.getCurrField not in validPile):
                    continue

                if newPile.getCurrField == "FF":
                    moves.insert(0, newPile)  # Prioritize jumps
                    self.availablePos(newPile, color, moves, False)

        return moves 
        
    def updateBoard(self, board):
        self.board = board