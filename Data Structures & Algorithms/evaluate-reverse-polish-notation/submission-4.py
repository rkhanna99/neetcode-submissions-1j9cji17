class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize a stack
        stack = []

        # Iterate through the tokens
        for token in tokens:
            print(stack)
            if token == "+" or token == "-" or token == "*" or token == "/":
                # Pop the last 2 values from the stack
                val_2 = int(stack.pop())
                val_1 = int(stack.pop())

                # Initialize the result and perform the operation
                result = 0
                
                if token == "+":
                    result = val_1 + val_2
                elif token == "-":
                    result = val_1 - val_2
                elif token == "*":
                    result = val_1 * val_2
                elif token == "/":
                    result = int(float(val_1) / val_2)

                stack.append(result)
            else:
                stack.append(token)

        return int(stack.pop())