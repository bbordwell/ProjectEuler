import unittest

from Euler96 import Board

class Euler96TestCase(unittest.TestCase):
    """Tests for Euler96.py"""

    def test_Board_solve(self):
        """Can Board solve a board that requires only Sole Candidate logic"""
        testBoard = Board([0, 0, 3, 0, 2, 0, 6, 0, 0, 9, 0, 0, 3, 0, 5, 0, 0, 1, 0, 0, 1, 8,
         0, 6, 4, 0, 0, 0, 0, 8, 1, 0, 2, 9, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 6, 7, 0,
          8, 2, 0, 0, 0, 0, 2, 6, 0, 9, 5, 0, 0, 8, 0, 0, 2, 0, 3, 0, 0, 9, 0, 0, 5, 0, 1, 0, 3, 0, 0])
        testBoard.soleCandidateSolveAttempt()
        self.assertEqual(testBoard.board,[4, 8, 3, 9, 2, 1, 6, 5, 7, 9, 6, 7, 3, 4, 5, 8, 2, 1, 2, 5,
                                          1, 8, 7, 6, 4, 9, 3, 5, 4, 8, 1, 3, 2, 9, 7, 6, 7, 2, 9, 5,
                                          6, 4, 1, 3, 8, 1, 3, 6, 7, 9, 8, 2, 4, 5, 3, 7, 2, 6, 8, 9, 
                                          5, 1, 4, 8, 1, 4, 2, 5, 3, 7, 6, 9, 6, 9, 5, 4, 1, 7, 3, 8, 2])
        self.assertEqual(testBoard.solvedBoard,True)
        self.assertEqual(testBoard.validBoard,True)

    def test_Board_invalid_board(self):
        """Gives Board an invalid starting board and tests that Board.validBoard gets set to False"""
        testBoard = Board([5, 0, 3, 0, 2, 0, 6, 0, 0, 9, 0, 0, 3, 0, 5, 0, 0, 1, 0, 0, 1, 8,
         0, 6, 4, 0, 0, 0, 0, 8, 1, 0, 2, 9, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 6, 7, 0,
          8, 2, 0, 0, 0, 0, 2, 6, 0, 9, 5, 0, 0, 8, 0, 0, 2, 0, 3, 0, 0, 9, 0, 0, 5, 0, 1, 0, 3, 0, 0])
        testBoard.soleCandidateSolveAttempt()
        self.assertEqual(testBoard.validBoard,False)

    def test_unsolvable_board(self):
        """Try to solve a board that can not be solved by only sole candidate logic, test that the board is still marked as valid and not solved"""
        testBoard = Board([0, 0, 0, 0, 0, 0, 9, 0, 7, 0, 0, 0, 4, 2, 0, 1, 8, 0, 0, 0, 0, 7, 0, 5, 0,
                           2, 6, 1, 0, 0, 9, 0, 4, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 5, 0,
                           7, 0, 0, 9, 9, 2, 0, 1, 0, 8, 0, 0, 0, 0, 3, 4, 0, 5, 9, 0, 0, 0, 5, 0, 7, 0, 0, 0, 0, 0, 0])
        testBoard.soleCandidateSolveAttempt()
        self.assertEqual(testBoard.validBoard,True)
        self.assertEqual(testBoard.solvedBoard,False)

    def test_already_solved(self):
        """Gives Board an already solved valid board and tests that it marks is as solved and valid"""
        testBoard = Board([4, 8, 3, 9, 2, 1, 6, 5, 7, 9, 6, 7, 3, 4, 5, 8, 2, 1, 2, 5, 1, 8, 7, 6, 4,
                           9, 3, 5, 4, 8, 1, 3, 2, 9, 7, 6, 7, 2, 9, 5, 6, 4, 1, 3, 8, 1, 3, 6, 7, 9,
                           8, 2, 4, 5, 3, 7, 2, 6, 8, 9, 5, 1, 4, 8, 1, 4, 2, 5, 3, 7, 6, 9, 6, 9, 5, 4, 1, 7, 3, 8, 2])
        testBoard.soleCandidateSolveAttempt()
        self.assertEqual(testBoard.solvedBoard,True)
        self.assertEqual(testBoard.validBoard,True)

    def test_already_solved_invalid_input(self):
        """Inputs what appears to be an already solved board, but it is invalid"""
        testBoard = Board([8, 8, 3, 9, 2, 1, 6, 5, 7, 9, 6, 7, 3, 4, 5, 8, 2, 1, 2, 5, 1, 8, 7, 6, 4,
                           9, 3, 5, 4, 8, 1, 3, 2, 9, 7, 6, 7, 2, 9, 5, 6, 4, 1, 3, 8, 1, 3, 6, 7, 9,
                           8, 2, 4, 5, 3, 7, 2, 6, 8, 9, 5, 1, 4, 8, 1, 4, 2, 5, 3, 7, 6, 9, 6, 9, 5, 4, 1, 7, 3, 8, 2])
        testBoard.soleCandidateSolveAttempt()
        self.assertEqual(testBoard.solvedBoard,False)
        self.assertEqual(testBoard.validBoard,False)

    def test_unique_candidate_column(self):
        testBoard = Board([0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                           0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0])
        testBoard.uniqueCandidatecolumn(0)
        self.assertEqual(testBoard.board[63],4)
        self.assertEqual(testBoard.solvedBoard,False)
        self.assertEqual(testBoard.validBoard,True)

    def test_unique_candidate_row(self):
        testBoard = Board([0, 0, 0, 0, 0, 0, 5, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                           0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        testBoard.uniqueCandidateRow(0)
        self.assertEqual(testBoard.board[7],4)
        self.assertEqual(testBoard.solvedBoard,False)
        self.assertEqual(testBoard.validBoard,True)

    def test_unique_candidate_block(self):
        testBoard = Board([0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 
                           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                           4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        testBoard.uniqueCandidateBlock(0)
        self.assertEqual(testBoard.board[10],4)
        self.assertEqual(testBoard.validBoard,True)
        self.assertEqual(testBoard.solvedBoard,False)

if __name__ == '__main__':
    unittest.main()