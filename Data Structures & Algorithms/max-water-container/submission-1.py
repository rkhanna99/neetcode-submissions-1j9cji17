class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        # Set 2 indicies (One at the beginning and one at the end)
        start_index = 0
        end_index = len(heights) - 1

        # Start moving both indices
        while start_index < end_index:
            curr_area = min(heights[start_index], heights[end_index]) * (end_index - start_index)

            # Update if needed
            if curr_area > max_area:
                max_area = curr_area

            # Move the pointer depending on the height
            if heights[start_index] > heights[end_index]:
                end_index -= 1
            else:
                start_index += 1

        return max_area