class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Initialize the max area
        max_area = 0

        # Initialize a stack that will be used to keep track of heights
        stack = []

        # Boolean value to indicate that we did indeed pop an element
        popped = False

        # Iterate through our heights
        for index, height in enumerate(heights):
            if len(stack) > 0:
                # Case where we encounter a smaller height we can't extend the rectangle fully
                while stack and stack[-1][1] > height:
                    # Calculate area of value at the top of the stack and indicate that we popped it
                    last_val = stack[-1]
                    curr_area = (index - last_val[0]) * last_val[1]
                    if curr_area > max_area:
                        max_area = curr_area
                    stack.pop()
                    popped = True
                # If we did have to pop the value we can move the index back all the way to the last element that was popped
                if popped == True:
                    stack.append((last_val[0], height))
                    popped = False
                else:
                    stack.append((index, height))
            else:
                stack.append((index, height))

        # For any elements still in the stack we know that they meet the conditions to go to the end of the heights array
        # So we calculate the area for each of the remaining values
        for element in stack:
            curr_area = (len(heights) - element[0]) * element[1]
            if curr_area > max_area:
                max_area = curr_area

        return max_area

        