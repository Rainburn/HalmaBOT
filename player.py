import time, datetime

class Player :

    def __init__(self, color):
        if (color == "RED") or (color == "R"):
            self.player_color = color
            self.player_turn = 1
        else :
            self.player_color = "GREEN"
            self.player_turn = 2

    def getTurn(self) :
        return self.player_turn

    def getColor(self) :
        return self.player_color

    def __str__(self) :
        return "HUMAN"


timer_stop = datetime.datetime.utcnow() + datetime.timedelta(seconds=5)
while True :
    x = input("input something :")
    print(x)
    if datetime.datetime.utcnow() > timer_stop :
        print("Timer Complete")
        break

