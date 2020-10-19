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

print()

while True :
    bot_count = int(input("Total Bot (1 / 2) : "))
    if (bot_count == 1) or (bot_count == 2) :
        break

game = Game(size_input, time_limit_input, bot_count)

# TO DO ---> CONTINUE THE GAME's EXECUTION CHRONOLOGICALLY
