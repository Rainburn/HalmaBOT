from board import Board
from player import Player

class Game :
    
    def __init__(self, board_size, time_limit, player_color):
        self.board = Board(board_size)
        self.time_limit = time_limit
        self.player = Player(player_color)
        self.turn = 1

    def nextTurn(self):
        self.turn = self.turn + 1

    def getTurn(self):
        return (self.turn % 2)

    def checkWinStatus(self):
        # Check whether someone has win the game
        return "SOMEONE HAS WON THE GAME"

    def checkTurnValidity(self, row_init, col_init, row_final, col_final):
        # Check Turn Validity
        return "RETURN WHETHER IT IS VALID OR NOT"

