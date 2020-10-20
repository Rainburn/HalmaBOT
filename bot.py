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
        moves = self.nextMove(color)
        best_move = None
        if max:
            best_val = float("-inf")
        else:
            best_val = float("inf")

        #basis
        if (depth == 3) or (self.checkwin("R", state)) or (self.checkwin("G", state)):
            return self.objFunc(color, state)

        #rekurens
        for i in range(len(moves)):
            #move: pindahin pion 
            initial_row = moves[i][0].getRow()
            initial_col = moves[i][0].getCol()   
            final_row = moves[i][1].getRow()
            final_col = moves[i][1].getCol()
            state.swapPosition(initial_row, initial_col, final_row, final_col)

            #panggil rekursif
            val, selected_move = self.minimax(depth+1, color, not max)
                
            #undo movenya
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
                move[1] = self.availablePos(currPile, color) #Destination Pile

                moves.append(move)

    def checkValidMove(self, selected_pawn, color, moves=None, row_fin, col_fin) :

        row_init = selected_pawn.getRow()
        col_init = selected_pawn.getCol()
        
        if (not(self.checkValidMoveByInBox(row_fin, col_fin))) :
            print("Invalid By InBox")
            return False

        if (not(self.checkValidMoveByField(selected_pawn, row_fin, col_fin))) :
            print("Invalid By Valid")
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