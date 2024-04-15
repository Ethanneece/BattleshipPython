import random

class Battleship: 

    hit = "X"
    miss = "O"
    ocean = "~"

    # Creates a battleship game
    def __init__(self, boardSize, amountOfShips): 
        self.player1Board = []
        self.player2Board = []
        self.boardSize = boardSize

        # append arrays to players board to generate 2-d array for the board. 
        for _ in range(boardSize):
            self.player1Board.append([self.ocean] * boardSize)
            self.player2Board.append([self.ocean] * boardSize)

        self.player1Ships = []
        self.player2Ships = []

        minShipSize = 2
        maxShipSize = 5

        # Randomly generate what ship sizes are going to be used for this game
        self.ships = []
        for _ in range(amountOfShips):
            shipSize = random.randint(minShipSize, maxShipSize)
            self.ships.append(shipSize)

        self.firstPlayer = Player(1)
        self.secondPlayer = CPU('Easy', 2)

        

    # Turns the array board into a string that is more human readable
    def _makeBoardString(self, board):
        
        boardString = ""

        # Header generator.
        offset = 3
        boardString += "" + " " * offset
        start = 'A'
        for _ in range(self.boardSize):
            boardString += start + " "

            # https://www.w3schools.com/python/ref_func_ord.asp
            start = chr(ord(start) + 1)
        
        boardString += "\n"

        #Print each line 
        boardNumber = 1 
        for line in board:
            boardLine = " ".join(line)

            # https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals
            boardString += f'{boardNumber:2} {boardLine}'
            boardString += "\n"
            boardNumber += 1

        return boardString.rstrip()
    
    def _makeBoardWithShipsString(self, board, ships):

        boardString = ""

        #Header generator. 
        offset = 3
        boardString += "" + " " * offset
        start = 'A'
        for _ in range(self.boardSize):
            boardString += start + " "
            start = chr(ord(start) + 1)

        boardString += "\n"

        boardNumber = 1
        for y in range(self.boardSize):
            boardLine = ""
            for x in range(0, self.boardSize):
                if [x, y] in ships: 
                    boardLine += self.hit
                else: 
                    boardLine += board[x][y]
            
            boardString += f'{boardNumber:2} {" ".join(boardLine)}\n'
            boardNumber += 1

        return boardString.rstrip()
        

    # Prints out the board of the first player of the game
    def printPlayer1(self): 
        board = self._makeBoardString(self.player1Board)
        print(board)

    # Prints out the board of the second player of the game 
    def printPlayer2(self):
        board = self._makeBoardString(self.player2Board)
        print(board)

    def setPlayer1(self, player):
        self.firstPlayer = player

    def setPlayer2(self, player):
        self.secondPlayer = player 

    # Prints out both boards side by side player 1 first
    def printBoards(self):
        player1Board = self._makeBoardString(self.player1Board).split("\n")
        player2Board = self._makeBoardString(self.player2Board).split("\n")

        # Add +1 because the header is included in the split. 
        print(f'   {self.firstPlayer.getName()} Board\t\t   {self.secondPlayer.getName()} Board')
        for i in range(self.boardSize + 1):
            print(f'{player1Board[i]}\t\t{player2Board[i]}')
        print()

    # Generate random ships on the board 
    def _generateRandomShipsR(self, ships, amountOfShips):
        # Find an initial place to put the ship
        shipX = random.randint(0, self.boardSize - 1)
        shipY = random.randint(0, self.boardSize - 1)

        shipSize = self.ships[amountOfShips - 1]

        # Find a direction to generate ship 
        shipDirections = ["UP", "LEFT", "DOWN", "RIGHT"]
        shipDirection = shipDirections[random.randint(0, len(shipDirections) - 1)]

        # Check if we can place ship in random location
        shipXIter = shipX
        shipYIter = shipY
        for _ in range(shipSize):

            # X out of bounds check
            if shipXIter < 0 or shipXIter >= self.boardSize:
                return self._generateRandomShipsR(ships, amountOfShips)
            
            # Y out of bounds check
            if shipYIter < 0 or shipYIter >= self.boardSize:
                return self._generateRandomShipsR(ships, amountOfShips)
            
            # Checking if ship is already in board
            if [shipXIter, shipYIter] in ships: 
                return self._generateRandomShipsR(ships, amountOfShips)

            # Change direction 
            if shipDirection == "UP":
                shipYIter -= 1
            if shipDirection == "LEFT":
                shipXIter += 1
            if shipDirection == "DOWN":
                shipYIter += 1
            if shipDirection == "RIGHT":
                shipXIter -= 1
        
        # Place the ship in that location
        shipXIter = shipX
        shipYIter = shipY
        for _ in range(shipSize):
            ships.append([shipXIter, shipYIter])

            # Change direction 
            if shipDirection == "UP":
                shipYIter -= 1
            if shipDirection == "LEFT":
                shipXIter += 1
            if shipDirection == "DOWN":
                shipYIter += 1
            if shipDirection == "RIGHT":
                shipXIter -= 1

        if amountOfShips == 1: 
            return 
        
        return self._generateRandomShipsR(ships, amountOfShips - 1)


    def _generatePlayerShips(self):
        self._generateRandomShipsR(self.player1Ships, len(self.ships))
        self._generateRandomShipsR(self.player2Ships, len(self.ships))

    # Print ouut both players boards side by side with ships shown. 
    def printBoardWithShips(self): 
        player1Board = self._makeBoardWithShipsString(self.player1Board, self.player1Ships).split("\n")
        player2Board = self._makeBoardWithShipsString(self.player2Board, self.player2Ships).split("\n")

        # Add +1 because the header is included in the split.
        print("   Player 1 Board\t\t   Player 2 Board")
        for i in range(self.boardSize + 1):
            print(f'{player1Board[i]}\t\t{player2Board[i]}')

    # Return true if the game is over, false otherwise
    def _gameOver(self):
         return len(self.player1Ships) == 0 or len(self.player2Ships) == 0
    
    # Takes a shot on the board using ships to determine if the 
    # shot hit or not. 
    def takeShot(self, move, board, ships):
        
        if (move in ships):
            board[move[0]][move[1]] = self.hit
            ships.remove(move)
        else: 
            board[move[0]][move[1]] = self.miss
    
    # Run a game of battleship.
    def runGame(self):

        while not self._gameOver():
            self.printBoards()
            # Player 1 takes shot
            move = self.firstPlayer.makeMove(self.player2Board)
            self.takeShot(move, self.player2Board, self.player2Ships)
            
            # Player 2 takes shot
            move = self.secondPlayer.makeMove(self.player1Board)
            self.takeShot(move, self.player1Board, self.player1Ships)

        self.printBoards()
        
        # Checking who has zero ships to see who wins
        if len(self.player1Ships) == 0:
            print(self.secondPlayer.getName() + " Won!")
            return self.secondPlayer
        else:
            print(self.firstPlayer.getName() + " Won!")
            return self.firstPlayer
        
    # Run the game without printing out the board. 
    def runGameNoPrint(self):
        while not self._gameOver():
            # Player 1 takes shot
            move = self.firstPlayer.makeMove(self.player2Board)
            self.takeShot(move, self.player2Board, self.player2Ships)
            
            # Player 2 takes shot
            move = self.secondPlayer.makeMove(self.player1Board)
            self.takeShot(move, self.player1Board, self.player1Ships)
        
        # Checking who has zero ships to see who wins
        if len(self.player1Ships) == 0:
            print(self.secondPlayer.getName() + " Won!")
            return self.secondPlayer
        
        else:
            print(self.firstPlayer.getName() + " Won!")
            return self.firstPlayer
        


class CPU: 

    difficultyLevels = ["Easy", 'Medium', 'Hard']

    def __init__(self, difficulty, number): 
        self.shots = []

        self.difficulty = difficulty
        self.number = number

        if (not difficulty in self.difficultyLevels):
            print("Difficulty does not exist ")
            print(f'Setting difficulty to {self.difficultyLevels[0]}')
            difficulty = self.difficultyLevels[0]

    def makeMove(self, board):

        move = None 
        if self.difficulty == "Easy":
            move = self.easyMove(board)

        if self.difficulty == "Medium":
            move = self.mediumMove(board)
        
        if self.difficulty == "Hard":
            move = self.hardMove(board)

        self.shots.append(move)

        return move
    
    def getName(self):
        return "CPU " + str(self.number)
    
    def getShots(self): 
        return self.shots

    
        
    # Makes a move for the easy CPU
    # Heuristic: 
    #   - Takes a random shot on the board 
    def easyMove(self, board): 
        boardSize = len(board)

        randomX = random.randint(0, boardSize - 1)
        randomY = random.randint(0, boardSize - 1)

        while [randomX, randomY] in self.shots: 
            randomX = random.randint(0, boardSize - 1)
            randomY = random.randint(0, boardSize - 1)

        return [randomX, randomY]


    # Makes a move for the medium CPU
    # Heurstic: 
    #   - If there is a hit on the board, 
    #       - Find potential places a ship could be and fire at it
    #   - Takes a random shot on the board
    def mediumMove(self, board):

        boardSize = len(board)
        potentialHits = self._potentialHits(board)

        if len(potentialHits) != 0:
            return random.choice(potentialHits)
        
        randomShot = [random.randint(0, boardSize - 1), random.randint(0, boardSize - 1)]

        while randomShot in self.shots: 
            randomShot = [random.randint(0, boardSize - 1), random.randint(0, boardSize - 1)]

        return randomShot 
    
    # Makes a move for the hard CPU.
    # Heuristic: 
    #   - If there is a hit on the board, 
    #       - Find a potential places a ship could be and fire at it 
    #   - Takes a shot at a polarized version of the board
    def hardMove(self, board):

        boardSize = len(board)
        potentialHits = self._potentialHits(board)


        if len(potentialHits) != 0:
            return random.choice(potentialHits)
        
        polarShot = [random.randint(0, boardSize - 1), random.randint(0, boardSize - 1)]

        while (polarShot[0] + polarShot[1]) % 2 != 0 or polarShot in self.shots:
            polarShot = [random.randint(0, boardSize - 1), random.randint(0, boardSize - 1)]


        return polarShot 

    # Returns all the potential positions where a ship might be on a board 
    def _potentialHits(self, board): 
        boardSize = len(board)
        hits = []
        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == Battleship.hit:
                    hits.append([x, y])
        
        potentialHits = []
        for hit in hits:
             up = [hit[0] - 1, hit[1]]
             left = [hit[0], hit[1] + 1]
             down = [hit[0] + 1, hit[1]]
             right = [hit[0], hit[1] - 1]

             surrondingHits = [up, left, down, right]
             for potential in surrondingHits: 

                # Check if potential hit is on board and is an ocean space
                if potential[0] >= 0 and potential[0] < boardSize and potential[1] >= 0 and potential[1] < boardSize: 
                    if board[potential[0]][potential[1]] == battleship.ocean: 
                        potentialHits.append(potential)

        return potentialHits

# Player class takes in input 
class Player: 

    def __init__(self, playerNumber):
        self.shots = []

        self.playerNumber = playerNumber 

    def makeMove(self, board):

        boardSize = len(board)

        userInput = input("Enter where you want to shoot: ")

        # Expected to be in the format {Letter Number}
        # Example: A 1
        coords = userInput.split(" ")

        # Didn't get proper coordinates
        if len(coords) != 2: 
            print(f'Input was not correct: {userInput}\n Expected: {"{Letter Number}"}')
            return self.makeMove(board) 
        
        # Didn't get proper coordinates
        # First input wasn't 1 character long 
        if len(coords[0]) > 1: 
            print(f'Input was not correct: {userInput}\n Expected {"{Letter Number}"}')
            return self.makeMove(board)
        
        # Didn't get proper coordinates
        # Second input wasn't a number
        if not coords[1].isnumeric():
            print(f'Input was not correct: {userInput}\n Expected {"{Letter Number}"}')
            return self.makeMove(boardSize)

        firstCoord = ord(coords[0]) - ord('A')
        secondCoord = int(coords[1]) - 1

        # Checking boundary on first coord
        if firstCoord < 0 and firstCoord < boardSize: 
            print(f'Coord {coords[0]} not in range')
            return self.makeMove(boardSize)
        
        # Checking boundary on second coord
        if secondCoord < 0 and secondCoord < boardSize:
            print(f'Coord {coords[1]} not in range')
            return self.makeMove(boardSize)
        
        return [secondCoord, firstCoord]
    
    def getName(self):
        return "Player " + str(self.playerNumber)
        

if __name__=='__main__':

    battleship = Battleship(10, 4)
    battleship.setPlayer1(CPU("Easy", "Easy"))
    battleship.setPlayer2(CPU("Medium", "Medium"))
    battleship._generatePlayerShips()
    results = {}
    results[CPU("Easy", "Easy").getName()] = 0
    results[CPU("Medium", "Medium").getName()] = 0
    for _ in range(100):
        results[battleship.runGameNoPrint().getName()] += 1
        battleship = Battleship(10, 4)
        battleship.setPlayer1(CPU("Easy", "Easy"))
        battleship.setPlayer2(CPU("Medium", "Medium"))
        battleship._generatePlayerShips()

    print(results)