# Welcome to my Battleships game. The rules are as follow:
# 1. The grid size is changeable by the player, it goes without saying that the larger the grid, the more difficult it is to win
# 2. The computer places 5 ships within the grid and the player tries sink the computer's ships using board coordinates
# 3. The turn counter is limited to 10 shots per player and at the end of the game if the player does not sink all ships, computer wins
# 4. Ships that are hit are marked with  "X" and shots missed are marked with "()"
# 5. If the player sinks all the ships, the computer Loses, otherwise the computer Wins
# To play the game, please input the grid size and when prompted input the coordinates for your shots
# Good Luck, Have Fun!
import random

# Creating the gameboard, "I" was ommited in order to escape confusion
class GameBoard:
    def __init__(self,board):
        self.board=board
#Creating a dictionary for the coordinates
    def lettersToNumbers():
        letters_numbers={"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7, "J":8, "K":9}
        return letters_numbers
#Printing the board and Grid
    def printBoard(self):
        print(" A B C D E F G H J K")
        print(" +-+-+-+-+-+-+-+-+-+")
        row_num= 1
        for row in self.board:
            print("%d|%s|"% (row_num, "|".join(row)))
            row_num+=1

print("Hello World")