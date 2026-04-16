class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Take the prefix product
        prefix = [1 for i in range(len(nums))]

        prefix_product = 1
        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] * prefix_product
            prefix_product = prefix[i]

        # Take the suffix product
        suffix = [1 for i in range(len(nums))]

        suffix_product = 1
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i + 1] * suffix_product
            suffix_product = suffix[i]

        result = [1 for i in range(len(nums))]
        for i in range(0, len(nums)):
            result[i] = prefix[i] * suffix[i]

        return result