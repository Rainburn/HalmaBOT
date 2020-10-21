# from game import Game
from board import Board
from pawn import *
import numpy as np
import random

class bot:
    def __init__(self, color):
        # self.pawns = []
        # for i in range(size):
        #     for j in range(size):
        #         if (i + j <= 3) and color = "RED" or color = "R":
        #             self.pawns.append(Pawn(i, j, "RED"))
        #
        #         elif (2 * size - (i + j) <= 5) and color = "GREEN" or color = "G":
        #             self.pawns.append(Pawn(i, j, "GREEN"))
        #
        #         else :
        #             break

        if (color == "RED") or (color == "R"):
            self.player_color = "R"
            self.player_turn = 1
        else :
            self.player_color = "G"
            self.player_turn = 0 # 2 % 2 = 0
            
    def __str__(self):
        return "BOT2"

    def getTurn(self) :
        return self.player_turn

    def getColor(self) :
        return self.player_color


    def checkwin(self, color,board):
        win = True
        size = board.getSize()
        if (color == "R"):
            for i in range(size):
                for j in range(size):
                    if (2 * size - (i + j) <= 5):
                        pile = board.getPile(i, j)
                        print(str(pile))
                        if (str(pile) == "x") or (str(pile) == "G") :
                            win = False
        elif (color == "G"):
            for i in range(size):
                for j in range(size):
                    if (i + j <= 3):
                        pile = board.getPile(i,j)
                        if (str(pile) == "x") or (str(pile) == "R") :
                            win = False
        return win

    def objectifFunction(self, color, board):
        valueR = 0
        valueG = 0
        n = board.getSize()
        opponent = ""

        if (color == "R"):
            opponent = "G"
        elif (color == "G"):
            opponent = "R"

        win = self.checkwin(color, board)
        print(win)
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
        while True:
            temp = random.choice(board.game_board)
            if str(temp) == "X" and temp.getCol() >= pawn.getCol() and temp.getRow() >= pawn.getRow() and  (game.checkValidMove(pawn, temp.getCol(), temp.getRow())):
                break
        return temp

    def localSearch(self, board, pawn):
        best_move = pawn
        board_temp = board
        while True:
            current = self.objectifFunction( pawn.color, board)
            print(current)
            print("asfdgdhjgadsdfghjgfdsadfghjgfds")
            succesor = self.generateRandomSuccesor(board_temp, best_move)
            board_temp.swapPosition(best_move.getRow(), best_move.getCol(), succesor.getRow(), succesor.getCol())
            new = self.objectifFunction( pawn.color, board_temp)
            if current > new:
                board_temp.swapPosition(succesor.getRow(), succesor.getCol(), best_move.getRow(), best_move.getCol())
                break
            # best_move = succesor

        return  board_temp
        # kalu mau akses row,col target tinggal best_move.getRow(), best_move.getCol()

    def generateChild(self, board, color):
        child = []
        board.printBoard()
        for i in range(board.getSize()):
            for j in range(board.getSize()):
                if str(board.getPile(i,j)) == color:
                    board_child = self.localSearch(board, board.getPile(i,j))
                    board_child.printBoard()
                    child.append(move,board_child)
        return child

    def minimax(self, board, depth, color, max = True, a = float("-inf"), b = float("inf")):
        #variabel dan move
        best_move = None
        if max:
            best_val = float("-inf")
            moves = self.generateChild(board, color)
        else:
            best_val = float("inf")
            moves = self.generateChild(board, "R" if color == "G" else "G")



        #basis
        if (depth == 3) or (self.checkwin(board,"R")) or (self.checkwin(board,"G")):
            return self.objectifFunction(pawn.color, board), best_move

        for move in moves:
            # move.board_child.printBoard()
            val, _ = self.minimax(move.board_child,depth-1,move.move.color,False,a,b)

            if max and val > best_val:
                    best_val = val
                    best_move = move.board_child
                    a = max(a, val)

            if not max and val < best_val:
                    best_val = val
                    best_move = move.board_child
                    b = min(b, val)

        return best_val, best_move
