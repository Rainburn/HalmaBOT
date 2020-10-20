class Player :

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
        return "HUMAN"




