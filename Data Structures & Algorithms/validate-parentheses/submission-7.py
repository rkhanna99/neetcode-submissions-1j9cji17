class Solution:
    def isValid(self, s: str) -> bool:
        # Base case
        if len(s) <= 1:
            return False

        # Initialize a stack
        stack = []

        # Iterate through each character in the string
        for c in list(s):
            # Add any opening parantheses to the stack
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                # Check what type of closing parantheses it is and then pop from stack if valid
                if c == ')' and stack[-1] != '(':
                    return False
                elif c == '}' and stack[-1] != '{':
                    return False
                elif c == ']' and stack[-1] != '[':
                    return False
                
                stack.pop()

        if len(stack) > 0:
            return False
        else:
            return True

