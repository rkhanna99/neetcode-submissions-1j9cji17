class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Setup our 2 pointers
        index1, index2 = 0, len(heights) - 1

        # Initialie the maximum area we will return
        maximum_area = 0

        # Iterate through the heights using 2 pointers
        while index1 < index2:
            # Calculate the current area
            curr_area = (min(heights[index1], heights[index2]) * abs(index1 - index2))
            
            # Set the maximum area if applicable
            if curr_area > maximum_area:
                maximum_area = curr_area

            # Move the pointers
            if heights[index1] > heights[index2]:
                index2 = index2 - 1
            else:
                index1 = index1 + 1
        
        return maximum_area
            