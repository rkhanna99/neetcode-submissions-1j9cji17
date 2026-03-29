class Solution:
    def trap(self, height: List[int]) -> int:
        max_area = 0

        # Set 2 indices (One at the beginning and then one at the end)
        start_index = 0
        end_index = len(height) - 1

        # To get max water held at each position we need to get the min value of the max left height and right height - current pos height
        # Get max left height at each position
        curr_max_left = 0
        max_left_pos = []

        for value in height:
            max_left_pos.append(curr_max_left)
            if value > curr_max_left:
                curr_max_left = value 

        curr_max_right = 0
        max_right_pos = []

        for value in reversed(height):
            max_right_pos.append(curr_max_right)
            if value > curr_max_right:
                curr_max_right = value

        max_right_pos.reverse()
        

        # Iterate through the height array
        for i in range(0, len(height)):
            curr_value = min(max_left_pos[i], max_right_pos[i]) - height[i]
            if curr_value > 0:
                max_area += curr_value

        return max_area 


            