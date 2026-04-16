class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # We have 9 rows, 9 Columns, and 9 Squares
        rows_set = [set() for i in range(9)]
        cols_set = [set() for i in range(9)]
        squares_set = [set() for i in range(9)]

        for row in range(0, len(board)):
            for col in range(0, len(board)):
                curr = board[row][col]
                
                curr_square = self.getCurrSquare(row, col)
                # If the character is a "." we just skip over it
                if curr == ".":
                    continue

                if curr in rows_set[row] or curr in cols_set[col] or curr in squares_set[curr_square]:
                    return False

                rows_set[row].add(curr)
                cols_set[col].add(curr)
                squares_set[curr_square].add(curr)
        
        return True

    def getCurrSquare(self, row, col):
        if row <= 2:
            if col <= 2:
                return 0
            elif col <= 5:
                return 1
            elif col <= 8:
                return 2
        elif row <= 5:
            if col <= 2:
                return 3
            elif col <= 5:
                return 4
            elif col <= 8:
                return 5
        elif row <= 8:
            if col <= 2:
                return 6
            elif col <= 5:
                return 7
            elif col <= 8:
                return 8


        