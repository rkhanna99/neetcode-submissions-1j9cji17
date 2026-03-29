class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Base Case (One token)
        if len(tokens) == 1:
            return int(tokens[0])

        # Initialize a stack for calculations
        stack = []

        # Iterate through the tokens and do the calculation with a stack
        for t in tokens:
            if t == "+":
                element_2 = stack.pop()
                element_1 = stack.pop()
                stack.append(element_1 + element_2)
            elif t == "-":
                element_2 = stack.pop()
                element_1 = stack.pop()
                stack.append(element_1 - element_2)
            elif t == "*":
                element_2 = stack.pop()
                element_1 = stack.pop()
                stack.append(element_1 * element_2)
            elif t == "/":
                element_2 = stack.pop()
                element_1 = stack.pop()
                stack.append(int(float(element_1) / element_2))
            else:
                stack.append(int(t))

            print(stack)

        return stack[-1]
