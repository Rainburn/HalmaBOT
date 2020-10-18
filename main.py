from board import Board
from game import Game

print()
print()
print("------------WELCOME-------------")
player_name = str(input("Your Name : "))

while True :
    size_input = int(input("Game Board Size (8 / 10 / 16) : "))

    if ((size_input == 8) or (size_input == 10) or (size_input == 16)) :
        break
    print("Please give the size correctly")

time_limit_input = int(input("Time Limit Input (in Second) : "))

while True :
    player_color = str(input("Choose Color : R (Red) / G (Green) : "))

    if ((player_color == "R") or (player_color == "G") or (player_color == "r") or (player_color == "g")) :
        break
    print("Please choose the color correctly")


game = Game(size_input, time_limit_input, player_color)
