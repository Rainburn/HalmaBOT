from game import Game
from board import Board
from pawn import *

def checkwin(color, state):
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


def objFunc(color, board):
    valueR = 0
    valueG = 0
    n = board.getSize()
    now = pawn.Empty()

    for i in range(n):
        for j in range (n):
            now = board.getPile(i, j)
            if pawn.str(now) == "R":
                valueR += i + j
            elif pawn.str(now) == "G":
                valueG += (2*n + 2 - (i + j))
            else:
                continue
    
    if (color == "R"):
        value = valueR - valueG
    elif (color == "G"):
        value = valueG - valueR
    return value

def minimax(depth, color, max=True, state):
    #possible moves from state
    moves = nextmove(color, state) #array of array, isinya pawn, col, row
    values = []
    #basis
    if (checkwin("R", state) or checkwin("G", state)):
        return moves[0] #isinya pawn, col, row
    
    #rekurens
    #bingung brok
    #idenya ada array moves, dicobain satu2

    for i in range len(moves):
        values[i] = objFunc(color, moves[i])

    if max:
        bestval = max(values)
        bestmove = moves[bestval]
    elif not max:
        bestval = min(values)
        bestmove = moves[bestval]

    #mesti return bestmove
    
def bot(color, board):
    abc