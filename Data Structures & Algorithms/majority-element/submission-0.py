class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Create a map
        num_map = {}

        # Iterate through each number
        for num in nums:
            if num in num_map:
                num_map[num] += 1
            else:
                num_map[num] = 1

        # Iterate through each key in the map
        for key in num_map:
            if num_map[key] > (len(nums) / 2):
                return key