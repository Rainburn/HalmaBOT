class Player :

    def __init__(self, color):
        self.player_color = color
        if (color == "RED") or (color == "R"):
            self.player_turn = 1
        else :
            self.player_turn = 2

    def getTurn(self) :
        return self.player_turn

    def __str__(self) :
        return "HUMAN"

        

