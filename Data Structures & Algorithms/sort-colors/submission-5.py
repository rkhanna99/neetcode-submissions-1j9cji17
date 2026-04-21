class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right = 0, len(nums) - 1
        i = 0

        # Start moving the pointers
        while i <= right:
            curr = nums[i]
            if curr == 0:
                nums[i] = nums[left]
                nums[left] = curr
                i += 1
                left += 1
            elif curr == 2:
                nums[i] = nums[right]
                nums[right] = curr
                right -= 1
            else:
                i += 1