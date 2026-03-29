class MinStack:

    def __init__(self):
        # Main stack
        self.stack = []

        # Stack to track the current minimum
        self.min_stack = []

    def push(self, val: int) -> None:
        # Add the element to the main stack
        self.stack.append(val)

        # Add the element to the min stack
        if len(self.stack) > 1:
            # Append the current min val if less than val
            if val < self.min_stack[-1]:
                self.min_stack.append(val)
            else:
                min_val = self.min_stack[-1]
                self.min_stack.append(min_val)
        else:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if len(self.stack) == 0:
            return None
        else:
            return self.min_stack[-1]
