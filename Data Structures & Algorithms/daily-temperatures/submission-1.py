class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0 for temp in temperatures]

        # Set up a stack (monotonically decreasing)
        stack = []

        for index, value in enumerate(temperatures):
            
            # Check if the current value is greater than the ones on the stack
            while stack and value > stack[-1][1]:
                prev_index, prev_value = stack.pop()
                output[prev_index] = index - prev_index
                    
            stack.append((index, value))

            print(stack)

        return output

