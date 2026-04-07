class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Set the left pointer
        left = 0

        # Set the count
        count = 1

        # Start iterating through the array at the 2nd index
        for i in range(1, len(nums)):
            if nums[left] != nums[i]:
                left += 1
                nums[left] = nums[i]
                count += 1
                

        return count
