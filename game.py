from board import Board
from player import Player

class Game :
    
    self.players = []

    def __init__(self, board_size, time_limit, bot_count):
        self.board = Board(board_size)
        self.time_limit = time_limit
        self.bot_count = bot_count
        self.turn = 1
        self.game_finished = False

        if (bot_count == 1) :
            print("RED Takes First Turn, Green Takes Second")

            while True :
                player_color = str(input("Choose Color : R (Red) / G (Green) : "))

                if ((player_color == "R") or (player_color == "G")) :
                    break
                print("Please choose the color correctly")
            
            self.players.append(Player(player_color))

            # After this, append BOT to self.players with the remaining unchosen color

        else : # Bot Count = 2 (ALL PLAYERS ARE BOT)
            # Append BOTS to self.players
            print("Append BOTS HERE")

    def play(self) :

        while not (self.game_finished) :
            
            turn = self.getTurn()
            in_play = self.getPlayerToTurn()

            # if player is HUMAN
            if (str(in_play) == "HUMAN") :
                # Turn of Timer
                while True :
                    selected_pawn = 


    def getPlayerToTurn(self) :
        turn = self.getTurn()
        for player in self.players :
            if (player.getTurn() == turn) :
                return player


    def nextTurn(self):
        self.turn = self.turn + 1

    def getTurn(self):
        return (self.turn % 2)

    def checkValidPickPawn(self, row, col) :
        pawn_selected = self.board.getPile(row, col)
        current_turn = self.getTurn()

        if (str(pawn_selected) == "R") and (current_turn == 1) :
            return True
        
        elif (str(pawn_selected) == "G") and (current_turn == 2) :
            return True

        else :
            return False

        

    def checkWinStatus(self):
        # Check whether someone has win the game

        greenWin = True
        # Check whether green wins the game
        for i in range(4) :
            for j in range(4 - i) :

                pile = self.board.getPile(i, j)
                if (str(pile) == "x") or (str(pile) == "R") :
                    greenWin = False

        if (greenWin) :
            return "Green WINS"

        # Green doesn't win, check Red
        redWin = True
        for i in range(4) :
            for j in range(4 - i) :
                row = self.board.getSize() - (i + 1)
                col = self.board.getSize() - (j + 1)

                pile = self.board.getPile(row, col)
                if (str(pile) == "x") or (str(pile) == "G") :
                    redWin = False
            
        if (redWin) :
            return "Red WINS"

        return False


        return "SOMEONE HAS WON THE GAME"

    def checkTurnValidity(self, row_init, col_init, row_final, col_final):
        # Check Turn Validity
        return "RETURN WHETHER IT IS VALID OR NOT"

