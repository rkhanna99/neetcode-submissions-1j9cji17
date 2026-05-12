class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        # Count the number of unique numbers
        unique = 1

        # Set the left and right pointers
        left = 0
        right = 1

        while right < len(nums):
            # Move the right if we have a duplicate
            while right < len(nums) and nums[left] == nums[right]:
                right += 1

            if right < len(nums):
                nums[left + 1] = nums[right]
                left += 1
                unique += 1

        return unique
            