import random

class Battleship: 

    hit = "X"
    miss = "O"
    ocean = "~"

    # Creates a battleship game
    # Needs 
    #   - Generate a list for both players board being boardsize
    #   - Fill list of both players boards with oceans
    #   - Create a list to hold both players ships locations
    #   - Create a list to hold randomly generated ship sizes 
    #       - Later used for generating ships on the player boards
    # Optional: 
    #   - Set the first and second player of the game 
    def __init__(self, boardSize, amountOfShips): 
        pass        

    # Turns the array board into a string that is more human readable
    # Needs 
    #   - Row at the top to specify columns
    #   - Column at the left side to specifiy rows 
    #   - A grid pattern representing the battleship game 
    # Example
    #   -   A B C
    #   - 1 ~ ~ ~ 
    #   - 2 ~ ~ ~
    #   - 3 ~ ~ ~
    def _makeBoardString(self, board):
        pass

    # Make board string but instead of just returning the board
    # also return where all the ships are currently located on the board. 
    # Example
    #   -   A B C
    #   - 1 ~ X ~ 
    #   - 2 ~ X ~
    #   - 3 ~ X ~  
    def _makeBoardWithShipsString(self, board, ships):
        pass

    # Prints out the board of the first player of the game
    def printPlayer1(self): 
        pass

    # Prints out the board of the second player of the game 
    def printPlayer2(self):
        pass

    # Sets player 1
    # Example: 
    #   - battleship.setPlayer1(Player(1))
    def setPlayer1(self, player):
        pass

    # Sets player 2
    # Example: 
    #   - battleship.setPlayer2(Player(2))
    def setPlayer2(self, player):
        pass

    # Prints out both boards side by side player 1 first
    # Example: 
    #   - First    Second
    #   -   A B C    A B C 
    #   - 1 X X X  1 ~ X ~
    #   - 2 ~ ~ ~  2 ~ X ~
    #   - 3 ~ ~ ~  3 ~ X ~
    def printBoards(self):
        pass

    # Generate random ships on the board
    # Needs: 
    #   - Fill player ships with the correct amount of ships
    #       - Make sure the ships are on the board 
    #       - Make sure ships are not overlapping 
    def _generateRandomShipsR(self, ships, amountOfShips):
        pass

    # Generates ships for both players
    # Needs to run before the game starts. 
    def _generatePlayerShips(self):
        pass

    # Print out both players boards side by side with ships shown. 
    def printBoardWithShips(self): 
        pass

    # Return true if the game is over, false otherwise
    def _gameOver(self):
        pass
    
    # Takes a shot on the board using ships to determine if the 
    # shot hit or not. 
    def takeShot(self, move, board, ships):
        pass
    
    # Run a game of battleship.
    def runGame(self):
        pass
        
    # Run the game without printing out the board. 
    def runGameNoPrint(self):
        pass

class CPU: 

    difficultyLevels = ["Easy", 'Medium', 'Hard']

    def __init__(self, difficulty, number): 
        pass

    def makeMove(self, board):
        pass
        
    # Makes a move for the easy CPU
    # Heuristic: 
    #   - Takes a random shot on the board 
    def easyMove(self, board): 
        pass


    # Makes a move for the medium CPU
    # Heurstic: 
    #   - If there is a hit on the board, 
    #       - Find potential places a ship could be and fire at it
    #   - Takes a random shot on the board
    def mediumMove(self, board):
        pass
    
    # Makes a move for the hard CPU.
    # Heuristic: 
    #   - If there is a hit on the board, 
    #       - Find a potential places a ship could be and fire at it 
    #   - Takes a shot at a polarized version of the board
    def hardMove(self, board):
        pass

    # Returns all the potential positions where a ship might be on a board 
    # Determined by looking at where all hits are on the board, and then 
    def _potentialHits(self, board): 
        pass

# Player class takes in input 
class Player: 

    # Init for the player
    def __init__(self, playerNumber):
        pass

    #Makes  a move for the player 
    def makeMove(self, board):
        pass
    
    #Gets the name of the player. 
    def getName(self):
        pass
        

#Start game here.
if __name__=='__main__':
    pass