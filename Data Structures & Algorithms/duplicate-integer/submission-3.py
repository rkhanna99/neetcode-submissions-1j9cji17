class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_dict = {}

        # Iterate through each value in nums
        for num in nums:
            # If the number is not already in the map
            if num not in num_dict.keys():
                num_dict[num] = 1
                continue

            if num_dict[num] == 1:
                return True

        return False