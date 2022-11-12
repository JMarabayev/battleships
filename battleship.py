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
        letters_numbers={"A":0, "B":1, "C":2, "D":3, "E":4, "F":5, "G":6, "H":7}
        return letters_numbers
#Printing the board and Grid
    def printBoard(self):
        print(" A B C D E F G H")
        print(" +-+-+-+-+-+-+-+")
        row_num= 1
        for row in self.board:
            print("%d|%s|"% (row_num, "|".join(row)))
            row_num+=1

# Creating Battleship Class (Taken from tutorial mentioned in README)
class Battleship:
    def __init__(self, board):
        self.board=board
    def generateShips(self):
        for i in range(5):
            self.x_row, self.y-column = random.randint(0, 7), random.randint(0, 7)
            while self.board[self.x_row, self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            self.board[self.x_row,self.y_column]="X"
        return self.board
# Getting user Input 
def getUserInput(self):
    try:
        x_row = input("Please Select the row coorinate (1-8)")
        while x_row not in '12345678':
            print("You are either out of bounds, or don't know what numbers are")
            x_row = input("Please Select the X coorinate (A-H)")
        y_column = input("Please Select the column coordinate (A-H)").upper()
        while y_column not in 'ABCDEFGH':
            print("You are either out of bounds, or don't know what Letters are")
            y_column = input("Please Select the column coordinate (A-H)").upper()
        return int(x_row)-1, GameBoard.lettersToNumbers()[y_column]
    except ValueError and KeyError:
        print("Invalid Choice")
        return self.getUserInput()
    #Counting Ships that were hit
    def HitCount():
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships
# Playing the game
def playGame():
    computer_board = GameBoard([[" "]*8 for i in range(8)])
    user_board = GameBoard([[" "]*8 for i in range(8)])
    Battleship.generateShips(computer_board)
    tries = 10
    while tries < 0:
        GameBoard.printBoard(user_board)
        user_x_row, user_y_column = Battleship.getUserInput(object)