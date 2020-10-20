from board import Board
from player import Player
from pawn import Pile, Pawn, Empty
from bot import Bot
import time, datetime

class Game :

    def __init__(self, board_size, time_limit, bot_count):
        self.board = Board(board_size)
        self.players = []
        self.time_limit = time_limit
        self.bot_count = bot_count
        self.turn = 1
        self.game_finished = False

        if (bot_count == 1) :
            print("RED Takes First Turn, Green Takes Second")
            player_color = "U"
            another_color = "U"

            while True :
                player_color = str(input("Choose Color : R (Red) / G (Green) : "))

                if ((player_color == "R") or (player_color == "G")) :
                    break
                print("Please choose the color correctly")
            
            self.players.append(Player(player_color))

            # After this, append BOT to self.players with the remaining unchosen color

            if (player_color == "R") :
                another_color = "G"
            else :
                another_color = "R"
            
            self.players.append(Bot(another_color, self.board))


        # For Testing Only

        elif (bot_count == 0) :
            print("RED Takes First Turn, Green Takes Second")
            player_color = "U"
            another_color = "U"

            while True :
                player_color = str(input("Choose Color : R (Red) / G (Green) : "))

                if ((player_color == "R") or (player_color == "G")) :
                    break
                print("Please choose the color correctly")

            another_color = "U"
            if (player_color == "R") :
                another_color = "G"
                    
            else : 
                another_color = "R"


            self.players.append(Player(player_color))
            self.players.append(Player(another_color))

        else : # TO DO ---> Bot Count = 2 (ALL PLAYERS ARE BOT)
            # Append BOTS to self.players

            self.players.append(Bot("R", self.board))
            self.players.append(Bot("G", self.board))


    def play(self) :

        while not (self.game_finished) :
            
            turn = self.getTurn()
            in_play = self.getPlayerToTurn()
            self.board.printBoard()
            print()
            print(in_play.getColor(), "'s TURN. Num Turn : ", self.turn)
            print()

            # if player is HUMAN
            if (str(in_play) == "HUMAN") :
                
                # Turn on Timer
                timer_stop = datetime.datetime.utcnow() + datetime.timedelta(seconds=self.time_limit)
                exit_by_timeout = False

                pawn_row = -1
                pawn_col = -1
                while True : # Picking Pawn until Valid Pawn Selected
                    select_row = int(input("Pawn's Row : "))
                    select_col = int(input("Pawn's Col : "))

                    if (datetime.datetime.utcnow() > timer_stop) : # Timeout break
                        exit_by_timeout = True
                        break
                    
                    if (self.checkValidPickPawn(select_row, select_col)) :
                        pawn_row = select_row
                        pawn_col = select_col
                        print("Pawn Selected")
                        print()
                        break
                    
                    else :
                        print("Select your pawn correctly")
                        print()
                
                if (exit_by_timeout) : # Timeout
                    print()
                    print("Timeout")
                    print()
                    break

                pawn_selected = self.board.getPile(select_row, select_col)

                # Move Pawn to Someplace
                target_valid_row = -1
                target_valid_col = -1
                while True : # Check if Turn is Valid
                    target_row = int(input("Target's Row : "))
                    target_col = int(input("Target's Col : "))

                    if (datetime.datetime.utcnow() > timer_stop) : # Timeout break
                        exit_by_timeout = True
                        break

                    # if move is valid, then break
                    if (self.checkValidMove(pawn_selected, target_row, target_col)) :
                        target_valid_row = target_row
                        target_valid_col = target_col
                        break
                        
                    else :
                        print()

                if (exit_by_timeout) : # Timeout
                    print()
                    print("Timeout")
                    print()
                    break

                # Move the Pawn
                self.movePawnTo(pawn_selected, target_valid_row, target_valid_col)

                win_status = self.checkWinStatus()
                if (win_status) :
                    print(win_status)
                    print()
                    self.game_finished = True
                    break

                self.nextTurn()


            else : # TO DO ---> BOT's TURN
                # TO DO --> Turn On Timer Here

                in_play.updateBoard(self.board)
                color = in_play.getColor()
                value, move = in_play.minimax(0, color)
                print(move)

                initial_row = move[0].getRow()
                initial_col = move[0].getCol()

                target_row = move[1].getRow()
                target_col = move[1].getCol()

                self.board.swapPosition(initial_row, initial_col, target_row, target_col)

                # do turn as bot's desires
                self.nextTurn()
                



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
        
        elif (str(pawn_selected) == "G") and (current_turn == 0) :
            return True

        else :
            return False


    def fieldCheck(self, row, col) :
        # Returns RF (Red Field), FF (Free Field), GF (Green Field)

        if (row + col <= 3) :
            return "RF"
        
        elif (2 * self.board.getSize() - (row + col) <= 5) :
            return "GF"
        
        else :
            return "FF"

    def checkValidMoveByField(self, selected_pawn, row, col) :
        initial_field = selected_pawn.getInitField()
        curr_field = selected_pawn.getCurrField()
        target_field = self.fieldCheck(row, col)

        if (curr_field == target_field) : # Stay in the same Field
            return True
        
        else : # Move to another field

            if (initial_field == "RF") : # Red Pawn
                if (curr_field == "FF") and (target_field == "RF") : # From Free Field, back to Home
                    return False
                
                elif (curr_field == "GF") and (target_field != "GF") : # Getting out from Target Field
                    return False

                else :
                    return True

            else : # Green Pawn
                if (curr_field == "FF") and (target_field == "GF") : # From Free Field, back to Home
                    return False
                
                elif (curr_field == "RF") and (target_field != "RF") : # Getting out from Target Field
                    return False

                else :
                    return True


    def checkValidMoveByInBox(self, row, col) : # Check whether the move is out of the board

        if (row >= self.board.getSize()) or (row < 0) :
            return False
        
        if (col >= self.board.getSize()) or (col < 0) :
            return False

        return True

    def checkValidMoveByEmpty(self, row, col) :
        pile = self.board.getPile(row, col)

        if (str(pile) == "x") :
            return True

        else :
            return False

    def checkValidMove(self, selected_pawn, row_fin, col_fin) :

        row_init = selected_pawn.getRow()
        col_init = selected_pawn.getCol()
        
        if (not(self.checkValidMoveByInBox(row_fin, col_fin))) :
            print("Invalid By InBox")
            return False

        if (not(self.checkValidMoveByField(selected_pawn, row_fin, col_fin))) :
            print("Invalid By Field")
            return False

        if (not(self.checkValidMoveByEmpty(row_fin, col_fin))) :
            print("Invalid By Not Empty")
            return False

        
        # 1st Type Move, to adjacent tile

        if (abs(row_init - row_fin) <= 1) and (abs(col_init - col_fin) <= 1) :
            return True

        # Diagonal Moves

        else : 
            queuePileToExpand = []
            queuePileToExpand.append(selected_pawn)
            possibleMove = []
            # Append all possible moves to possibleMove
            while (queuePileToExpand) :
                expanding_pile = queuePileToExpand.pop(0)
                # Checking All Possibilities
                expanding_pile_row = expanding_pile.getRow()
                expanding_pile_col = expanding_pile.getCol()

                # Iterate clockwise from East to North East

                # East
                if (self.board.canMoveEast(expanding_pile_row, expanding_pile_col, 2)) and (not(self.board.canMoveEast(expanding_pile_row, expanding_pile_col))) : # Skipping a Pawn
                    empty_pile = self.board.takeEastPile(expanding_pile_row, expanding_pile_col, 2)
                    
                    already_exist = False
                    for pile in possibleMove :
                        if (pile.getRow() == empty_pile.getRow()) and (pile.getCol() == empty_pile.getCol()) :
                            already_exist = True

                    if (not(already_exist)) :
                        queuePileToExpand.append(empty_pile)
                        possibleMove.append(empty_pile)

                # South East
                if (self.board.canMoveSouthEast(expanding_pile_row, expanding_pile_col, 2)) and (not(self.board.canMoveSouthEast(expanding_pile_row, expanding_pile_col))) : # Skipping a Pawn
                    empty_pile = self.board.takeSouthEastPile(expanding_pile_row, expanding_pile_col, 2)

                    already_exist = False
                    for pile in possibleMove :
                        if (pile.getRow() == empty_pile.getRow()) and (pile.getCol() == empty_pile.getCol()) :
                            already_exist = True

                    if (not(already_exist)) :
                        queuePileToExpand.append(empty_pile)
                        possibleMove.append(empty_pile)

                # South
                if (self.board.canMoveSouth(expanding_pile_row, expanding_pile_col, 2)) and (not(self.board.canMoveSouth(expanding_pile_row, expanding_pile_col))) : # Skipping a Pawn
                    empty_pile = self.board.takeSouthPile(expanding_pile_row, expanding_pile_col, 2)
                    
                    already_exist = False
                    for pile in possibleMove :
                        if (pile.getRow() == empty_pile.getRow()) and (pile.getCol() == empty_pile.getCol()) :
                            already_exist = True

                    if (not(already_exist)) :
                        queuePileToExpand.append(empty_pile)
                        possibleMove.append(empty_pile)

                # South West
                if (self.board.canMoveSouthWest(expanding_pile_row, expanding_pile_col, 2)) and (not(self.board.canMoveSouthWest(expanding_pile_row, expanding_pile_col))) : # Skipping a Pawn
                    empty_pile = self.board.takeSouthWestPile(expanding_pile_row, expanding_pile_col, 2)
                    
                    already_exist = False
                    for pile in possibleMove :
                        if (pile.getRow() == empty_pile.getRow()) and (pile.getCol() == empty_pile.getCol()) :
                            already_exist = True

                    if (not(already_exist)) :
                        queuePileToExpand.append(empty_pile)
                        possibleMove.append(empty_pile)

                # West
                if (self.board.canMoveWest(expanding_pile_row, expanding_pile_col, 2)) and (not(self.board.canMoveWest(expanding_pile_row, expanding_pile_col))) : # Skipping a Pawn
                    empty_pile = self.board.takeWestPile(expanding_pile_row, expanding_pile_col, 2)
                    
                    already_exist = False
                    for pile in possibleMove :
                        if (pile.getRow() == empty_pile.getRow()) and (pile.getCol() == empty_pile.getCol()) :
                            already_exist = True

                    if (not(already_exist)) :
                        queuePileToExpand.append(empty_pile)
                        possibleMove.append(empty_pile)

                # North West
                if (self.board.canMoveNorthWest(expanding_pile_row, expanding_pile_col, 2)) and (not(self.board.canMoveNorthWest(expanding_pile_row, expanding_pile_col))) : # Skipping a Pawn
                    empty_pile = self.board.takeNorthWestPile(expanding_pile_row, expanding_pile_col, 2)
                    
                    already_exist = False
                    for pile in possibleMove :
                        if (pile.getRow() == empty_pile.getRow()) and (pile.getCol() == empty_pile.getCol()) :
                            already_exist = True

                    if (not(already_exist)) :
                        queuePileToExpand.append(empty_pile)
                        possibleMove.append(empty_pile)

                # North
                if (self.board.canMoveNorth(expanding_pile_row, expanding_pile_col, 2)) and (not(self.board.canMoveNorth(expanding_pile_row, expanding_pile_col))) : # Skipping a Pawn
                    empty_pile = self.board.takeNorthPile(expanding_pile_row, expanding_pile_col, 2)
                    
                    already_exist = False
                    for pile in possibleMove :
                        if (pile.getRow() == empty_pile.getRow()) and (pile.getCol() == empty_pile.getCol()) :
                            already_exist = True

                    if (not(already_exist)) :
                        queuePileToExpand.append(empty_pile)
                        possibleMove.append(empty_pile)

                # North East
                if (self.board.canMoveNorthEast(expanding_pile_row, expanding_pile_col, 2)) and (not(self.board.canMoveNorthEast(expanding_pile_row, expanding_pile_col))) : # Skipping a Pawn
                    empty_pile = self.board.takeNorthEastPile(expanding_pile_row, expanding_pile_col, 2)
                    
                    already_exist = False
                    for pile in possibleMove :
                        if (pile.getRow() == empty_pile.getRow()) and (pile.getCol() == empty_pile.getCol()) :
                            already_exist = True

                    if (not(already_exist)) :
                        queuePileToExpand.append(empty_pile)
                        possibleMove.append(empty_pile)

                # End of Iteration, check whether the final row and col in the possibleMove

            isValidMove = False
            for pile in possibleMove :
                if (pile.getRow() == row_fin) and (pile.getCol() == col_fin) :
                    isValidMove = True

            if (not(isValidMove)) :
                print("Invalid Turn, Not Possible to Jump")

            return isValidMove
                    
         
    def movePawnTo(self, selected_pawn, row, col) : # Just swap right away, valid checking will be conducted before this function
        
        row_init = selected_pawn.getRow()
        col_init = selected_pawn.getCol()
        target_field = self.fieldCheck(row, col)
        self.board.swapPosition(row_init, col_init, row, col)
        self.board.getPile(row, col).setCurrField(target_field)


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


