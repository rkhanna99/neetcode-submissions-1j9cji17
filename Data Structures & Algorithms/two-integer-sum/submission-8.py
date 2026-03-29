class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute Force: Target - nums[i] and see if in array
        # for i in range(0, len(nums)):
        #     difference = target - nums[i]
        #     j = i + 1
        #     while j < len(nums):
        #         if nums[j] == difference:
        #             return [i, j]
        #         j += 1

        # Two Pointer Solution:

        # First we need to sort the array (n log n)
        sorted_nums = []
        for index, value in enumerate(nums):
            sorted_nums.append([value, index])

        sorted_nums.sort()

        i = 0
        j = len(nums) - 1

        while i < j:
            curr_sum = sorted_nums[i][0] + sorted_nums[j][0]
            if curr_sum > target:
                j -= 1
            elif curr_sum < target:
                i += 1
            else:
                
                return [min(sorted_nums[i][1], sorted_nums[j][1]), max(sorted_nums[i][1], sorted_nums[j][1])]

        

