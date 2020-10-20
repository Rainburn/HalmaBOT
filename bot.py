from game import Game
from board import Board
from pawn import *

class Bot:


    def __init__(self, color, board):
        self.color = color
        self.board = board

    def checkwin(self, color, state=self.board):
        win = True
        if (color == "R"):
            for i in range(4) :
                for j in range(4 - i) :
                    row = state.getSize() - (i + 1)
                    col = state.getSize() - (j + 1)

                    pile = self.board.getPile(row, col)
                    if (str(pile) == "x") or (str(pile) == "G") :
                        win = False
        elif (color == "G"):
            for i in range(4) :
                for j in range(4 - i) :
                    pile = state.getPile(i, j)
                    if (str(pile) == "x") or (str(pile) == "R") :
                        win = False
        return win


    def objFunc(self, color, board=self.board):
        valueR = 0
        valueG = 0
        n = board.getSize()
        now = Pawn.Empty()
        opponent = ""

        if (color == "R"):
            opponent = "G"
        elif (color == "G"):
            opponent = "R"

        win = self.checkwin(color, board)
        lose = self.checkwin(opponent, board)

        if win:
            value = 99999
        elif lose:
            value = -99999
        else:
            for i in range(n):
                for j in range (n):
                    now = board.getPile(i, j)
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

    def minimax(self, depth, color, max = True, state=self.board):
        #variabel dan move
        moves = nextmove(color, state) #nextmove blom ada
        best_move = None
        if max:
            best_val = float("-inf")
        else:
            best_val = float("inf")

        #basis
        if (depth == 3) or (self.checkwin("R", state)) or (self.checkwin("G", state)):
            return self.objFunc(color, state)

        #rekurens
        for move in moves:
            #move: pindahin pion (ga yakin cara kerjanya gimana)
            initial_row = move.pawn.getRow()
            initial_col = move.pawn.getCol()
            final_row = move.row
            final_col = move.col
            state.swapPosition(initial_row, initial_col, final_row, final_col)

            #panggil rekursif
            val, selected_move = self.minimax(depth+1, color, not max)
                
            #undo movenya (ga yakin cara kerjanya)
            state.swapPosition(final_row, final_col, initial_row, initial_col)

        if max and (val > best_val):
            best_val = val
            best_move = selected_move
        if not max and (val V best_val):
            best_val = val
            best_move = selected_move

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

    def nextMove(self, color, board=self.board):
        moves = []
        for row in range(board.getSize()):
            for col in range(board.getSize()):

                currPile = board.getPile(row, col)

                if currPile != color:
                    continue

                move[0] = currPile #From Pile
                move[1] = ge

  
    # def minimaxi(self, depth, color, max=True, state):
    #     #possible moves from state
    #     moves = nextmove(color, state) #array of array, isinya Pawn, col, row
    #     values = []
    #     #basis
    #     if (checkwin("R", state) or checkwin("G", state)):
    #         return moves[0] #isinya Pawn, col, row
        
    #     #rekurens
    #     #bingung brok
    #     #idenya ada array moves, dicobain satu2

    #     for i in range(len(moves)):
    #         values[i] = objFunc(color, moves[i])

    #     if max:
    #         bestval = max(values)
    #         bestmove = moves[bestval]
    #     elif not max:
    #         bestval = min(values)
    #         bestmove = moves[bestval]

    #     #mesti return bestmove
        
    def bot(self, color, board):