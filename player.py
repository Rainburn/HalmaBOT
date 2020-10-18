class Player :

    def __init__(self, color):
        self.player_color = color
        if (color == "RED"):
            self.player_turn = 1
        else :
            self.player_turn = 2

    
    def pickPawn(self, game_board, row, col):
        pile_selected = game_board.getPile(row, col)
        

