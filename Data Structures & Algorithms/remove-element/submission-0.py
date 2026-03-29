class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Iterate through the nums and keep track of the index
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                i -= 1
            i += 1

        return len(nums)