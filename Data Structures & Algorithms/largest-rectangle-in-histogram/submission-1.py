class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Initialize a stack to keep track of the heights
        stack = []

        # Initialize a max area value
        max_area = 0

        # Boolean to indicate that we did pop
        popped = False

        # Iterate through the heights array
        for index, height in enumerate(heights):
            if len(stack) == 0:
                stack.append((index, height))
            else:
                # If the current height is greater we add it to the stack
                if height >= stack[-1][1]:
                    stack.append((index, height))
                else:
                    # Can't extend the rectangle further so we keep popping from the stack to maintain monotonic increasing
                    while stack and height < stack[-1][1]:
                        last_val = stack[-1]
                        # Compute the area and update if needed
                        curr_area = (index - last_val[0]) * last_val[1]
                        if curr_area > max_area:
                            max_area = curr_area
                        # Remove from the stack
                        stack.pop()
                        popped = True

                    # We can set the index of our new entry (if we popped we know the value can extend back to that spot)
                    if popped == True:
                        stack.append((last_val[0], height))
                        popped = False
                    else:
                        stack.append((index, height))

        # For any value left in the stack we know they can make it to the end of the heights arrays so we compute the area
        for index, value in stack:
            print(stack)
            curr_area = (len(heights) - index) * value
            if curr_area > max_area:
                max_area = curr_area

        return max_area 

