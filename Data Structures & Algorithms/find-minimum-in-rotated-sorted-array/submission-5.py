class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # Initialize the left and right pointers and a minimum value
        left, right = 0, len(nums) - 1

        minimum = 1001

        # Start the binary search process
        while left < right:
            print(f"Left: {left}, right: {right}")
            midpoint = (left + right) // 2
            if nums[left] > nums[right] and nums[midpoint] > nums[right]:
                left = midpoint + 1
                if nums[right] < minimum:
                    minimum = nums[right]
            elif nums[left] < nums[right] and nums[midpoint] < nums[right]:
                right = midpoint - 1
                if nums[left] < minimum:
                    minimum = nums[left]
            elif nums[midpoint] < nums[right] and nums[midpoint] < nums[left]:
                minimum = nums[midpoint]
                left = left + 1
                right = right - 1

        return minimum

