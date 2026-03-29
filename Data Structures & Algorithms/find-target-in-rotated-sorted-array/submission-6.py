class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Define a left and right pointer for binary search
        left, right = 0, len(nums) - 1

        # Start the binary search process
        while left <= right:
            midpoint = (left + right) // 2

            # Check if the target is at any og the current points
            if nums[midpoint] == target:
                return midpoint
            elif nums[left] == target:
                return left
            elif nums[right] == target:
                return right

            # Move the pointers
            # The left is sorted
            if nums[midpoint] > nums[right]:
                if target in range(nums[left], nums[midpoint]):
                    right = midpoint - 1
                else:
                    left = midpoint + 1
            else:
                if target in range(nums[midpoint], nums[right]):
                    left = midpoint + 1
                else:
                    right = midpoint - 1


            

        return -1