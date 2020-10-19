from pawn import Pawn, Empty

class Board :

    def __init__(self, size):
        self.size = size
        self.game_board = [[] for i in range(size)]

        for i in range(size):
            for j in range(size):
                if (i + j <= 3):
                    self.game_board[i].append(Pawn("RED"))

                elif (2 * size - (i + j) <= 5):
                    self.game_board[i].append(Pawn("GREEN"))
                
                else :
                    self.game_board[i].append(Empty())

    
    def swapPosition(self, col_initial, row_initial, col_final, row_final):
        temp = self.game_board[row_final][col_final]
        self.game_board[row_final][col_final] = self.game_board[row_initial][col_initial]
        self.game_board[row_initial][col_initial] = temp


    def getPile(self, row, col):
        return self.game_board[row][col]
        



    def printBoard(self):

        print()

        for i in range(self.size):
            for j in range(self.size):
                print(self.game_board[i][j], end=" ")
            
            print()

        print()
            


    def getSize(self):
        return self.size


