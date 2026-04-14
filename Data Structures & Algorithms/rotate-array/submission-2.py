class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Mod by length of the array to get the number of rotations
        rotations = k % len(nums)

        # Reverse the whole list
        left, right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # Reverse the first k elements:
        left, right = 0, rotations - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        # Reverse the last k elements:
        left, right = rotations, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1