class Solution:
    def trap(self, height: List[int]) -> int:
        # Setup our 2 pointers
        index1, index2 = 0, len(height) - 1

        # Initialize max area variable to return
        max_area = 0

        # Save the current max heights on left and right
        left_max_height = 0
        right_max_height = 0

        # Iterate through the heights array
        while index1 < index2:
            if height[index1] >= left_max_height:
                left_max_height = height[index1]
            else:
                max_area = max_area + (left_max_height - height[index1])
            
            if height[index2] >= right_max_height:
                right_max_height = height[index2]
            else:
                max_area = max_area + (right_max_height - height[index2])
            
            if height[index1] > height[index2]:
                index2 = index2 - 1
            else:
                index1 = index1 + 1
        return max_area
            