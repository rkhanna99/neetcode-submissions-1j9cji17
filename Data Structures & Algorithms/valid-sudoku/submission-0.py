class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # Check if a row is valid
        for row in board:
            seen = set()
            for num in row:
                if num != "." and num in seen:
                    return False
                seen.add(num)
            
        # Check if a column is valid
        for c in range(0, 9):
            seen = set()
            for r in range(0, 9):
                if board[r][c] != "." and board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        # Check each 3x3 subgrid
        for box_row in range(0, 9, 3):  # Starting rows of each subgrid
            for box_col in range(0, 9, 3):  # Starting columns of each subgrid
                seen = set()
                for r in range(box_row, box_row + 3):  # Rows in the subgrid
                    for c in range(box_col, box_col + 3):  # Columns in the subgrid
                        curr = board[r][c]
                        if curr != ".":
                            if curr in seen:
                                return False
                            seen.add(curr)
        return True


            