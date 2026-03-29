class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check the rows first
        for row in board:
            print(row)
            seen = set()
            for value in row:
                if value in seen and value != '.':
                    return False
                else:
                    seen.add(value)


        # Check the columns next
        for i in range(0, 9):
            seen = set()
            for j in range(0, 9):
                curr_value = board[j][i]
                if curr_value in seen and curr_value != '.':
                    return False
                else:
                    seen.add(curr_value)

        # Check each square
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                seen = set()
                for inner_i in range(i, i + 3):
                    for inner_j in range(j, j + 3):
                        curr_value = board[inner_i][inner_j]
                        print(seen)
                        if curr_value in seen and curr_value != '.':
                            return False
                        else:
                            seen.add(curr_value)


        return True