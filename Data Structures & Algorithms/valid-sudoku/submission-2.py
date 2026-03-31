class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Iterate through each row
        for row in board:
            curr_row_set = set()
            for num in row:
                if num in curr_row_set:
                    return False
                else:
                    if num != ".":
                        curr_row_set.add(num)

        # Iterate through each column
        for i in range(0, 9):
            curr_column_set = set()
            for j in range(0, 9):
                if board[j][i] in curr_column_set:
                    return False
                else:
                    if board[j][i] != ".":
                        curr_column_set.add(board[j][i])
                

        # Iterate through each of the 9 squares in a Sudoku board
        for row_start in range(0, 9, 3): 
            for col_start in range(0, 9, 3):
                
                curr_square_set = set()
                for i in range(row_start, row_start + 3):
                    for j in range(col_start, col_start + 3):
                        if board[i][j] in curr_square_set:
                            return False
                        else:
                            if board[i][j] != ".":
                                curr_square_set.add(board[i][j])
                

        return True