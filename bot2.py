from game import Game
from board import Board
from pawn import *
import numpy as np

class bot:
    def __init__(self, color):
        if (color == "RED") or (color == "R"):
            self.player_color = "R"
            self.player_turn = 1
        else :
            self.player_color = "G"
            self.player_turn = 0 # 2 % 2 = 0

    def getTurn(self) :
        return self.player_turn

    def getColor(self) :
        return self.player_color

    def __str__(self) :
        return "BOT"

    def objectifFunction(self, color, board):
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

    def generateRandomSuccesor(self, board, pawn):
        size = board.getSize()
        temp = Pawn.Empty()
        while str(temp) != "X" and temp.getCol() < pawn.getCol() and temp.getRow() < pawn.getRow() and not (game.checkValidMove(pawn, temp.getCol(), temp.getRow())) :
            temp = np.random.choice(board.game_board.ravel(),1,replace=False)
        return temp

    def localSearch(self, board, pawn):
        best_move = pawn
        board_temp = board
        while True:
            current = objectifFunction(self, pawn.color, board)
            succesor = self.generateRandomSuccesor(board_temp, best_move)
            board_temp.swapPosition(best_move.getRow(), best_move.getCol(), succesor.getRow(), succesor.getCol())
            new = objectifFunction(self, pawn.color, board_temp)
            if current > new:
                break
            best_move = succesor

        return best_move
        # kalu mau akses row,col target tinggal best_move.getRow(), best_move.getCol()

        
