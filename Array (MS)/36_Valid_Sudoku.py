class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.isValidRow(board) and self.isValidCol(board) and self.isValidSquare(board)

    def isValidRow(self, board):
        for row in board:
            checklist = []
            for unit in row:
                if unit != '.':
                    checklist.append(unit)

            if len(set(checklist)) != len(checklist):
                return False

        return True

    def isValidCol(self, board):
        for col in zip(*board):
            checklist = []
            for unit in col:
                if unit != '.':
                    checklist.append(unit)

            if len(set(checklist)) != len(checklist):
                return False

        return True

    def isValidSquare(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                checklist = []
                unit = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                for elem in unit:
                    if elem != '.':
                        checklist.append(elem)
                if len(set(checklist)) != len(checklist):
                    return False
        return True
