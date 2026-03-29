class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize a value for the minimum and the left/right pointers for binary search
        minimum = 1001
        left, right = 0, len(nums) - 1

        while left <= right:
            midpoint = (right + left) // 2

            # Update the minimum as needed
            if nums[midpoint] < minimum:
                minimum = nums[midpoint]

            # Move both left and right if midpoint is less then both
            if nums[left] > nums[midpoint] and nums[right] > nums[midpoint]:
                left = left + 1
                right = right - 1
            elif nums[left] < nums[midpoint] and nums[right] > nums[midpoint]:
                right = midpoint - 1
            else:
                left = midpoint + 1

        return minimum