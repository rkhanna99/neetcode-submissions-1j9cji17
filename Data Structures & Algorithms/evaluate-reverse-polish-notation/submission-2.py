class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Dict of operators
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x // y
        }
        # Initialize a stack
        stack = []

        for token in tokens:
            if token != "+" and token != "-" and token != "*" and token != "/":
                stack.append(int(token))
            else:
                print(stack)
                second_val = int(stack.pop())
                first_val = int(stack.pop())
                if token == "+":
                    curr_val = (first_val + second_val)
                elif token == "-":
                    curr_val = (first_val - second_val)
                elif token == "*":
                    curr_val = (first_val * second_val)
                elif token == "/":
                    curr_val = int(float(first_val) / second_val)
                stack.append(curr_val)
        
        return stack[-1]