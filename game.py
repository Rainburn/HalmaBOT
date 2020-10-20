from board import Board
from player import Player
from pawn import Pile, Pawn, Empty

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

        else : # TO DO ---> Bot Count = 2 (ALL PLAYERS ARE BOT)
            # Append BOTS to self.players
            print("Append BOTS HERE")

    def play(self) :

        while not (self.game_finished) :
            
            turn = self.getTurn()
            in_play = self.getPlayerToTurn()
            self.board.printBoard()
            print()
            print(in_play.getColor(), "'s TURN")
            print()

            # if player is HUMAN
            if (str(in_play) == "HUMAN") :
                # Turn on Timer
                pawn_row = -1
                pawn_col = -1
                while True : # Picking Pawn until Valid Pawn Selected
                    select_row = int(input("Pawn's Row : "))
                    select_col = int(input("Pawn's Col : "))

                    if (self.checkValidPickPawn(pawn_row, pawn_col)) :
                        pawn_row = select_row
                        pawn_col = select_col
                        break
                    
                    else :
                        print("Select your pawn correctly")
                        print()
                
                pawn_selected = self.board.getPile(select_row, select_col)

                # Move Pawn to Someplace
                target_valid_row = -1
                target_valid_col = -1
                while True : # Check if Turn is Valid
                    target_row = int(input("Target's Row : "))
                    target_col = int(input("Target's Col : "))

                    # if move is valid, then break
                    if (self.checkValidMove(pawn_selected, target_row, target_col)) :
                        target_valid_row = target_row
                        target_valid_col = target_col
                        break

                
                # Move the Pawn
                self.movePawnTo(pawn_selected, target_valid_row, target_valid_col)

                win_status = self.checkValidMove()
                if (win_status) :
                    print(win_status)
                    print()
                    self.game_finished = True
                    break

                self.nextTurn()


            else : # TO DO ---> BOT's TURN
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
        
        elif (str(pawn_selected) == "G") and (current_turn == 2) :
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

    def checkValidMoveByEmpty(self, row, col) :
        pile = self.board.getPile(row, col)

        if (str(pile) == "x") :
            return True

        else :
            return False

    def checkValidMove(self, selected_pawn, row_init, col_init, row_fin, col_fin) :
        
        if (not(self.checkValidMoveByInBox(row_fin, col_fin))) :
            return False

        if (not(self.checkValidMoveByField(selected_pawn, row_fin, col_fin))) :
            return False

        if (not(self.checkValidMoveByEmpty(row_fin, col_fin))) :
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

            return isValidMove
                    
         
    def movePawnTo(self, selected_pawn, row, col) : # Just swap right away, valid checking will be conducted before this function
        
        row_init = selected_pawn.getRow()
        col_init = selected_pawn.getCol()
        self.board.swapPosition(row_init, col_init, row, col)


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


