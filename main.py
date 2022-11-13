import random

# Creating the gameboard, "I" was ommited in order to escape confusion
class GameBoard:  
    def __init__(self, board):
        self.board = board

# Creating a dictionary for the coordinates
    def lettersToNumbers():
        letters_numbers={"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        return letters_numbers

# Printing the board and Grid
    def printBoard(self):
        print("  A B C D E F G H")
        print(" +-+-+-+-+-+-+-+-+")
        row_num= 1
        for row in self.board:
            print("%d|%s|" % (row_num, "|".join(row)))
            row_num+=1

# Creating Battleship Class (Taken from tutorial mentioned in README)
class Battleship:

# initialising the board
    def __init__(self, board):
        self.board = board

# creating computer ships
    def generateShips(self):
        for i in range(5):
            self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            self.board[self.x_row][self.y_column] = "X"
        return self.board

# Getting user Input 
    def getUserInput(self):
        try:
            x_row = input("Please Select the row coorinate (1-8)")
            while x_row not in '12345678':
                print("You are either out of bounds, or don't know what numbers are")
                x_row = input("Please Select the row coorinate (1-8)")

            y_column = input("Please Select the column coordinate (A-H)").upper()
            while y_column not in 'ABCDEFGH':
                print("You are either out of bounds, or don't know what Letters are")
                y_column = input("Please Select the column coordinate (A-H)").upper()
            return int(x_row)-1, GameBoard.lettersToNumbers()[y_column]
        except ValueError and KeyError:
            print("Invalid Choice")
            return self.getUserInput()
    #Counting Ships that were hit
    def count_hit_ships(self):
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships
# Playing the game
def playGame():
    computer_board = GameBoard([[" "] * 8 for i in range(8)])
    user_board = GameBoard([[" "]*8 for i in range(8)])
    Battleship.generateShips(computer_board)
    tries = 10
    while tries > 0:
        GameBoard.printBoard(user_board)
        user_x_row, user_y_column = Battleship.getUserInput(object)
        while user_board.board[user_x_row] [user_y_column] == '-' or user_board.board[user_x_row] [user_y_column] == 'X':
            print("You already tried that!")
            user_x_row, user_y_column = Battleship.getUserInput(object)
        if computer_board.board[user_x_row][user_y_column] == "X":
            print("You sunk 1 of my battleship!")
            user_board.board[user_x_row][user_y_column] = "X"
        else:
            print("You missed my battleship!")
            user_board.board[user_x_row][user_y_column] = "-"
        if Battleship.count_hit_ships(user_board) == 5:
            print("All Ships Sunk! You Win!!")
            break
        else:
            tries -= 1
            print(f'You have {tries} tries left')
            if tries == 0:
                print("You are out of shots, You lose!")
                GameBoard.printBoard(user_board)
                break
if __name__== '__main__':
    playGame()