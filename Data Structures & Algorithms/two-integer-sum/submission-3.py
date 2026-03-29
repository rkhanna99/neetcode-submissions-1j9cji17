class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ret_value = []

        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[j] == (target - nums[i]):
                    ret_value = [i, j]
                    return ret_value