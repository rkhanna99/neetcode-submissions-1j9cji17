class Solution:
    def isValid(self, s: str) -> bool:
        # Create a dictionary to match all appropriate parentheses
        char_dict = {'(':')', '{':'}', '[':']'}
        
        # Split the string
        input_list = list(s)
        
        # Initialize an empty stack
        stack = []

        for p in input_list:
            # Check if we have a forward parenthesis '(', '{', '['
            if p in char_dict:
                stack.append(p)
            else:
                if len(stack) != 0:
                    matching = char_dict[stack[-1]]
                    if matching != p:
                        return False
                    else:
                        stack.pop()
                else:
                    return False
        return len(stack) == 0