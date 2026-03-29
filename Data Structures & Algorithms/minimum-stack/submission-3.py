class MinStack:

    def __init__(self):
        # Initialize the stack to keep track of the elements
        self.stack = []

        # Initialize a stack to keep track of the smallest element at each stage
        self.min_stack = []

    def push(self, val: int) -> None:
        # Add the value to the top of the stack
        self.stack.append(val)

        # Check if have anything in the min_stack
        if len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            if self.min_stack[-1] > val:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[-1])

        print(self.min_stack)
        

    def pop(self) -> None:
        self.stack.pop()

        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
