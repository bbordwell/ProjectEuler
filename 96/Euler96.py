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
    def __init__(self, board):
        self.board = board
        self.updateBoard()

    def updateBoard(self):
        self.row0 = self.generateRow(0)
        self.row1 = self.generateRow(1)
        self.row2 = self.generateRow(2)
        self.row3 = self.generateRow(3)
        self.row4 = self.generateRow(4)
        self.row5 = self.generateRow(5)
        self.row6 = self.generateRow(6)
        self.row7 = self.generateRow(7)
        self.row8 = self.generateRow(8)
        self.collumn0 = self.generateCollumn(0)
        self.collumn1 = self.generateCollumn(1)
        self.collumn2 = self.generateCollumn(2)
        self.collumn3 = self.generateCollumn(3)
        self.collumn4 = self.generateCollumn(4)
        self.collumn5 = self.generateCollumn(5)
        self.collumn6 = self.generateCollumn(6)
        self.collumn7 = self.generateCollumn(7)
        self.collumn8 = self.generateCollumn(8)
        self.block1 = self.generateBlock(1)
        self.block2 = self.generateBlock(2)
        self.block3 = self.generateBlock(3)
        self.block4 = self.generateBlock(4)
        self.block5 = self.generateBlock(5)
        self.block6 = self.generateBlock(6)
        self.block7 = self.generateBlock(7)
        self.block8 = self.generateBlock(8)
        self.block9 = self.generateBlock(9)
    
    def generateRow(self,n):
        row = set()
        for cell in self.board[n*9:(n*9)+9]:
            if cell != 0:
                row.add(cell)
            else:
                pass
        return row

    def generateCollumn(self,n):
        collumn = set()
        for row in range(9):
            if self.board[n+(row*9)]:
                collumn.add(self.board[n+(row*9)])
        return collumn

    def generateBlock(self,n):
        block = set()
        whatCells = {1:(0,1,2,9,10,11,18,19,20),2:(3,4,5,12,13,14,21,22,23),
                     3:(6,7,8,15,16,17,24,25,26),4:(27,28,29,36,37,38,45,46,47),
                     5:(30,31,32,39,40,41,48,49,50),6:(33,34,35,42,43,44,51,52,53),
                     7:(54,55,56,63,64,65,72,73,74),8:(57,58,59,66,67,68,75,76,77),
                     9:(60,61,62,69,70,71,78,79,80)}
        for cell in whatCells[n]:
            if self.board[cell] != 0:
                block.add(self.board[cell])
        return block

    def whatRow(self,n):
        return n//9

    def whatCollumn(self,n):
        return n%9

    def whatBlock(self,n):
        whatCells = {1:(0,1,2,9,10,11,18,19,20),2:(3,4,5,12,13,14,21,22,23),
                     3:(6,7,8,15,16,17,24,25,26),4:(27,28,29,36,37,38,45,46,47),
                     5:(30,31,32,39,40,41,48,49,50),6:(33,34,35,42,43,44,51,52,53),
                     7:(54,55,56,63,64,65,72,73,74),8:(57,58,59,66,67,68,75,76,77),
                     9:(60,61,62,69,70,71,78,79,80)}
        for k,v in whatCells.items():
            if n in v:
                return k

    def whatCouldGoHere(self,n):
        notPossibles = set()
        rows = [self.row0,self.row1,self.row2,self.row3,self.row4,self.row5,self.row6,self.row7,self.row8]
        for notPossible in rows[self.whatRow(n)]:
            notPossibles.add(notPossible)
        collumns = [self.collumn0,self.collumn1,self.collumn2,self.collumn3,self.collumn4,self.collumn5,self.collumn6,self.collumn7,self.collumn8]
        for notPossible in collumns[self.whatCollumn(n)]:
            notPossibles.add(notPossible)
        blocks = [self.block1,self.block2,self.block3,self.block4,self.block5,self.block6,self.block7,self.block8,self.block9]
        for notPossible in blocks[self.whatBlock(n)-1]:
            notPossibles.add(notPossible)
        return {1,2,3,4,5,6,7,8,9} - notPossibles

    def checkCell(self,n):
        if len(self.whatCouldGoHere(n)) == 1:
            return True

    def nextSolve(self):
        for cell in range(81):
            if self.board[cell] == 0:
                if self.checkCell(cell):
                    ans = self.whatCouldGoHere(cell).pop()
                    self.board[cell] = ans
                    self.updateBoard()
                    return True
        return False

    def solveAttempt(self):
        while True:
            if not self.nextSolve():
                break

for board in boards2:
    boardInstance = Board(board)
    while True:
        if not boardInstance.nextSolve():
            break
    if 0 in boardInstance.board:
        print("could not solve")
    else:
        print(boardInstance.board)


