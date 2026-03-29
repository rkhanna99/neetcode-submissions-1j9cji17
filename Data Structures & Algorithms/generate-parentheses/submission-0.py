class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret_list = []

        def backtrack(current, open_count, closed_count):
            # If we have n open and closed parentheses
            if open_count == closed_count == n:
                ret_list.append(current)
                return

            # If we want to add a open parenthese
            if open_count < n:
                backtrack(current + "(", open_count + 1, closed_count)
            
            # If we want to add a closing parenthese
            if closed_count < open_count:
                backtrack(current + ")", open_count, closed_count + 1)
            
        backtrack("", 0, 0)
        return ret_list