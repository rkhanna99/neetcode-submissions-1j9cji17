class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0 for i in range(0,3)]

        for num in nums:
            buckets[num] += 1

        index = 0
        for i in range(0, 3):
            while buckets[i] != 0:
                nums[index] = i
                buckets[i] -= 1
                index += 1
        