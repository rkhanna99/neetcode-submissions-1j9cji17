class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1

        max_area = -1

        while left < right:
            # Calculate the current distance
            curr_area = (right - left) * min(heights[left], heights[right])
            if curr_area > max_area:
                max_area = curr_area

            # Determine how we move the pointers
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return max_area