#This block opens boards.txt and creates a list of all 50 boards
#The boards are converted into a list of 81 ints, read from left to right, top to bottom
boardsFile = open("boards.txt")
boardsList = []
for line in boardsFile:
    boardsList.append(line.strip())
boards = []
for x in range(0,500,10):
    boards.append(boardsList[x+1:x+10])
boards2 = []
for board in boards:
    transform = []
    for row in board:
        for cell in row:
            transform.append(int(cell))
    boards2.append(transform)

class Board:
    """This class represents a single sudoku board. Input a list of 81 ints for this initial board"""
    def __init__(self, board):
        self.board = board
        self.validBoard = True      #Assume the input is valid, update later if proven otherwise
        self.solvedBoard = False    #assume the input board is not solved, update later if proven otherwise
        self.updateBoard()

    def updateBoard(self):
        """This function updates the values for what numbers are in each row, column and block"""
        self.rows = [[], [], [], [], [], [], [], [], []]
        self.rows[0] = self.generateRow(0)
        self.rows[1] = self.generateRow(1)
        self.rows[2] = self.generateRow(2)
        self.rows[3] = self.generateRow(3)
        self.rows[4] = self.generateRow(4)
        self.rows[5] = self.generateRow(5)
        self.rows[6] = self.generateRow(6)
        self.rows[7] = self.generateRow(7)
        self.rows[8] = self.generateRow(8)
        self.columns = [[], [], [], [], [], [], [], [], []]
        self.columns[0] = self.generatecolumn(0)
        self.columns[1] = self.generatecolumn(1)
        self.columns[2] = self.generatecolumn(2)
        self.columns[3] = self.generatecolumn(3)
        self.columns[4] = self.generatecolumn(4)
        self.columns[5] = self.generatecolumn(5)
        self.columns[6] = self.generatecolumn(6)
        self.columns[7] = self.generatecolumn(7)
        self.columns[8] = self.generatecolumn(8)
        self.blocks = [[], [], [], [], [], [], [], [], []]
        self.blocks[0] = self.generateBlock(0)
        self.blocks[1] = self.generateBlock(1)
        self.blocks[2] = self.generateBlock(2)
        self.blocks[3] = self.generateBlock(3)
        self.blocks[4] = self.generateBlock(4)
        self.blocks[5] = self.generateBlock(5)
        self.blocks[6] = self.generateBlock(6)
        self.blocks[7] = self.generateBlock(7)
        self.blocks[8] = self.generateBlock(8)
    
    def generateRow(self,n):
        """Input a row number (0-8) and return a set of numbers known to be in that row"""
        row = []
        for cell in self.board[n*9:(n*9)+9]:
            if cell != 0 and cell not in row:
                row.append(cell)
            elif cell in row:
                self.validBoard = False
            else:
                pass
        return row

    def generatecolumn(self,n):
        """Input a column number (0-8) and return a set of numbers known to be in that column"""
        column = []
        for cell in self.cellsInColumn(n):
            if self.board[cell] and self.board[cell] not in column:
                column.append(self.board[cell])
            elif self.board[cell] in column:
                self.validBoard = False
        return column

    def generateBlock(self,n):
        """Input a block number (0-8) and return a set of numbers known to be in that block"""
        block = []
        for cell in self.cellsInBlock(n):
            if self.board[cell] != 0 and self.board[cell] not in block:
                block.append(self.board[cell])
            elif self.board[cell] in block:
                self.validBoard = False
        return block

    def whatRow(self,n):
        """Input a cell number, and return what row it is in"""
        return n//9

    def whatcolumn(self,n):
        """Input a cell number and return what column it is in"""
        return n%9

    def whatBlock(self,n):
        """Input a cell number and return what block it is in"""
        for block in range(9):
            if n in self.cellsInBlock(block):
                return block

    def whatCouldGoHere(self,n):
        """Input a cell number, and based on what is known of its row, cell and block return what numbers could logically fit"""
        notPossibles = set()
        for notPossible in self.rows[self.whatRow(n)]:
            notPossibles.add(notPossible)
        for notPossible in self.columns[self.whatcolumn(n)]:
            notPossibles.add(notPossible)
        for notPossible in self.blocks[self.whatBlock(n)]:
            notPossibles.add(notPossible)
        return {1,2,3,4,5,6,7,8,9} - notPossibles

    def checkCell(self,n):
        """Input a cell number and return True if the correct value for the cell can be deduced"""
        if len(self.whatCouldGoHere(n)) == 1:
            return True
        if len(self.whatCouldGoHere(n)) == 0:
            self.validBoard = False
        else:
            return False

    def nextSoleCandidate(self):
        """This function searches the board for the next square solvable by the sole candidate method and updates the board with that solve"""
        for cell in range(81):
            if self.board[cell] == 0:
                if self.checkCell(cell):
                    ans = self.whatCouldGoHere(cell).pop()
                    self.board[cell] = ans
                    self.updateBoard()
                    return True
        return False

    def soleCandidateSolveAttempt(self):
        "This function solves all cells that can be solved by the sole Candidate technique"
        while True:
            if not self.nextSoleCandidate():
                self.isSolved()
                break
        
    def isSolved(self):
        """This function checks if the board is completly solved. Returns True if so, False otherwise"""
        if 0 not in self.board and self.validBoard:
            self.solvedBoard = True
            return True
        else:
            return False
    
    def uniqueCandidatecolumn(self,column):
        """Input a column number and it will check that column for any square that can be solved using unique candidate"""
        leftToFind = [x for x in [1,2,3,4,5,6,7,8,9] if x not in self.columns[column]]
        for num in leftToFind:
            fitCounter = 0
            for cell in self.cellsInColumn(column):
                if self.board[cell] == 0 and num in self.whatCouldGoHere(cell):
                        fitCounter += 1
                        fitCell = cell
            if fitCounter == 1:
                self.board[fitCell] = num
                self.updateBoard()
                return True

    def uniqueCandidatecolumns(self):
        """This function checks all colums on the board for squares that can be solved using the unique candidate method"""
        anySolves = False
        for column in range(9):
            if self.uniqueCandidatecolumn(column):
                anySolves = True
        return anySolves

    def cellsInColumn(self,column):
        """Input a column number (0-8) and output all cell locations in that column as a list"""
        cells = []
        for row in range(9):
            cells.append(column+(row*9))
        return cells

    def cellsInRow(self,row):
        """Input a row number (0-8) and output all cell locations in that row as a list"""
        return list(range(row*9,(row*9)+9))

    def cellsInBlock(self,block):
        """Input a block number (0-8) and return a list of all cell locations in that block"""
        whatCells = {0:(0,1,2,9,10,11,18,19,20),1:(3,4,5,12,13,14,21,22,23),
                     2:(6,7,8,15,16,17,24,25,26),3:(27,28,29,36,37,38,45,46,47),
                     4:(30,31,32,39,40,41,48,49,50),5:(33,34,35,42,43,44,51,52,53),
                     6:(54,55,56,63,64,65,72,73,74),7:(57,58,59,66,67,68,75,76,77),
                     8:(60,61,62,69,70,71,78,79,80)}
        return whatCells[block]

    def uniqueCandidateRow(self,row):
        """Input a row number and solve any squares in that row that can be solved using the unique candidate technique"""
        leftToFind = [x for x in [1,2,3,4,5,6,7,8,9] if x not in self.rows[row]]
        for num in leftToFind:
            fitCounter = 0
            for cell in self.cellsInRow(row):
                if self.board[cell] == 0 and num in self.whatCouldGoHere(cell):
                    fitCounter += 1
                    fitCell = cell
            if fitCounter == 1:
                self.board[fitCell] = num
                self.updateBoard()
                return True

    def uniqueCandidateRows(self):
        """Check all rows on the board for cells that can be solved using the unique candidate method"""
        anysolves = False
        for row in range(9):
            if self.uniqueCandidateRow(row):
                anysolves = True
        return anysolves

    def uniqueCandidateBlock(self,block):
         """Input a block number and solve any squares in that block that can be solved using the unique candidate technique"""
         leftToFind = [x for x in [1,2,3,4,5,6,7,8,9] if x not in self.blocks[block]]
         for num in leftToFind:
             fitCounter = 0
             for cell in self.cellsInBlock(block):
                 if self.board[cell] == 0 and num in self.whatCouldGoHere(cell):
                     fitCounter += 1
                     fitCell = cell
             if fitCounter == 1:
                self.board[fitCell] = num
                self.updateBoard()
                return True

    def uniqueCandidateBlocks(self):
        """Check all blocks on the board for cells that can be solved using the unique candidate method"""
        anySolves = False
        for block in range(9):
            if self.uniqueCandidateBlock(block):
                anySolves = True
        return anySolves

    def simpleGuess(self):
        """Finds cells with only two possibilities and tries both, if one can be proven wrong without further guessing update the board with the correct guess"""
        for cell in range(81):
            if self.board[cell] == 0 and len(self.whatCouldGoHere(cell)) == 2:
                whats = list(self.whatCouldGoHere(cell))
                newBoard1 = Board(self.board[:])
                newBoard1.board[cell] = whats[0]
                newBoard2 = Board(self.board[:])
                newBoard2.board[cell] = whats[1]
                newBoard1.solveBoard(recursive=True)
                newBoard2.solveBoard(recursive=True)
                if newBoard1.validBoard != newBoard2.validBoard:
                    if newBoard1.validBoard:
                        self.board[cell] = whats[0]
                        self.updateBoard()
                        return True
                    if newBoard2.validBoard:
                        self.board[cell] = whats[1]
                        self.updateBoard()
                        return True
        return False
                    
    def solveBoard(self,recursive=False):
        """Try to solve the board using all techniques in this program"""
        while True:
            self.soleCandidateSolveAttempt()
            if self.validBoard == False:
                return False
            if self.solvedBoard == True:
                return True
            if self.uniqueCandidatecolumns():
                if self.validBoard == False:
                    return False
                if self.solvedBoard == True:
                    return True
                continue
            if self.uniqueCandidateRows():
                if self.validBoard == False:
                    return False
                if self.solvedBoard == True:
                    return True
                continue
            if self.uniqueCandidateBlocks():
                if self.validBoard == False:
                    return False
                if self.solvedBoard == True:
                    return True
                continue
            if recursive == False and self.simpleGuess():
                if self.validBoard == False:
                    return False
                if self.solvedBoard == True:
                    return True
                continue
            return False

def sixGuess(board):
    """This function is a terrible hack for grid 49, it trys all combinations of guesses for all cells that have two possibilities
    This only works if the board has exactly 6 cells that have two possibilites"""
    from itertools import product
    guesses = []
    cells = []
    for cell in range(81):
        if len(board.whatCouldGoHere(cell)) == 2:
            guesses.append(board.whatCouldGoHere(cell))
            cells.append(cell)
    guesses = list(product(guesses[0],guesses[1],guesses[2],guesses[3],guesses[4],guesses[5]))
    newBoards = []
    for guess in guesses:
        newBoards.append(Board(board.board[:]))
    for newBoard in range(len(guesses)):
        for cell in range(len(cells)):
            newBoards[newBoard].board[cells[cell]] = guesses[newBoard][cell]
    for newBoard in newBoards:
        if newBoard.solveBoard():
            return newBoard.board
    return False

#Solve all boards and create a list of all solutions    
solvedBoards = []
for n,grid in enumerate(boards2):
    board = Board(grid)
    if n != 48: #Grid 49 can't be solved by the logic currently in the board class
        if board.solveBoard():
            solvedBoards.append(board.board)
    else:   #Use special guessing function created for grid 49. Todo improve main logic so i can solve this board
        solvedBoards.append(sixGuess(board))

#Find the number represented by the top left most three cells and add them all together for the final answer to Euler 96
ans = 0
for board in solvedBoards:
    num = [str(x) for x in board[:3]]
    num = int(str().join(num))
    ans += num
print(ans)

