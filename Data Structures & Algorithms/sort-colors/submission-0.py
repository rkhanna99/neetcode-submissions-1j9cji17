class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Create our buckets
        buckets = [0 for i in range(3)]
        
        # Iterate through each value and increment the bucket
        for num in nums:
            buckets[num] += 1
            
        index = 0
        for i in range(0, 3):
            curr = buckets[i]
            while curr != 0:
                nums[index] = i
                curr -= 1
                index += 1
