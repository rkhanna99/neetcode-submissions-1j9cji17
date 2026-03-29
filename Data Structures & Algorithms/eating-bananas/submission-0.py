import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Set the left and right pointers for binary search
        left, right = 1, max(piles)

        ret_value = right

        # Start the binary search iteration
        while left <= right:
            midpoint = (left + right) // 2
            curr_hours = 0
            # Calculate the time taken to eat each pile with the midpoint serving as k
            for value in piles:
                hours_taken = math.ceil(value / midpoint)
                curr_hours = curr_hours + hours_taken
            # Update the ret_value if we have used less hours to eat all bananas
            if curr_hours <= h:
                if midpoint < ret_value:
                    ret_value = midpoint
                right = midpoint - 1
            else:
                left = midpoint + 1

        return ret_value
