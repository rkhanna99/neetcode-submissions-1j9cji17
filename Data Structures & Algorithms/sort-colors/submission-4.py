class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        left = 0
        right = len(nums) - 1

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