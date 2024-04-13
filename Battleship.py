import random

class Battleship: 

    hit = "X"
    miss = "O"
    ocean = "~"

    # Creates a battleship game
    def __init__(self, boardSize, amountOfShips): 
        self.player1Board = []
        self.player2Board = []

        for _ in range(boardSize):
            self.player1Board.append([self.ocean] * boardSize)
            self.player2Board.append([self.ocean] * boardSize)

        self.player1Ships = []
        self.player2Ships = []

        minShipSize = 2
        maxShipSize = 5

        self.ships = []
        for _ in range(amountOfShips):
            shipSize = random.randint(minShipSize, maxShipSize)
            self.ships.append(shipSize)

        self.boardSize = boardSize

    # Turns the array board into a string that is more human readable
    def _makeBoardString(self, board):
        
        boardString = ""

        #Header generator.
        offset = 3
        boardString += "" + " " * offset
        start = 'A'
        for _ in range(self.boardSize):
            boardString += start + " "
            start = chr(ord(start) + 1)
        
        boardString += "\n"

        #Print each line 
        boardNumber = 1 
        for line in board:
            boardLine = " ".join(line)
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

        print(self.ships)
        print(ships)

        boardNumber = 1
        for y in range(self.boardSize):
            boardLine = ""
            for x in range(self.boardSize + 1):
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

    # Prints out both boards side by side player 1 first
    def printBoards(self):
        player1Board = self._makeBoardString(self.player1Board).split("\n")
        player2Board = self._makeBoardString(self.player2Board).split("\n")

        for i in range(self.boardSize):
            print(f'{player1Board[i]}\t\t{player2Board[i]}')

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
            if shipXIter < 0 or shipXIter > self.boardSize:
                return self._generateRandomShipsR(ships, amountOfShips)
            
            # Y out of bounds check
            if shipYIter < 0 or shipYIter > self.boardSize:
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

    def printBoardWithShips(self): 
        player1Board = self._makeBoardWithShipsString(self.player1Board, self.player1Ships).split("\n")
        player2Board = self._makeBoardWithShipsString(self.player2Board, self.player2Ships).split("\n")

        for i in range(self.boardSize):
            print(f'{player1Board[i]}\t\t{player2Board[i]}')


battleship = Battleship(10, 3)
battleship._generatePlayerShips()
battleship.printBoardWithShips()