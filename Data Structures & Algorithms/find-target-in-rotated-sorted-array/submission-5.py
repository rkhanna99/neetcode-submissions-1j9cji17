class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            # Calculate the midpoint
            midpoint = (left + right) // 2

            # Check if the target is at the current midpoint
            if nums[midpoint] == target:
                return midpoint
            elif nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            
            # Determine which side is sorted
            if nums[midpoint] > nums[right]:
                # Left side must be sorted
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
