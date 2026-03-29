class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.stack) > 1:
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
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
