class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Array of sets for each row
        rows = [set() for i in range(0, 9)]

        # Array of sets for each column
        columns = [set() for i in range(0, 9)]

        # Array of sets for each square
        squares = [set() for i in range(0, 9)]

        for i in range(0, 9):
            for j in range(0, 9):
                # Set the current value
                curr_value = board[i][j]

                # Get curr square
                curr_square = self.get_square(i, j)

                # Check if it is "."
                if curr_value == ".":
                    continue
                else:
                    if curr_value in rows[i] or curr_value in columns[j] or curr_value in squares[curr_square]:
                        return False
                    else:
                        rows[i].add(curr_value)
                        columns[j].add(curr_value)
                        squares[curr_square].add(curr_value)

                    
        return True


    def get_square(self, row, col) -> int:
        if row <= 2:
            if col <= 2:
                return 0
            if col <= 5:
                return 1
            if col <= 8:
                return 2
        if row <= 5:
            if col <= 2:
                return 3
            if col <= 5:
                return 4
            if col <= 8:
                return 5
        if row <= 8:
            if col <= 2:
                return 6
            if col <= 5:
                return 7
            if col <= 8:
                return 8
            
