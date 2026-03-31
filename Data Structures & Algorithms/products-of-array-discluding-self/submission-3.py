class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Value at result[i] = Prefix[i] * Suffix[i]

        # Prefix
        prefix = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Suffix
        suffix = [1 for i in range(len(nums))]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        print(prefix)
        print(suffix)

        result = [1 for i in range(len(nums))]
        for i in range(0, len(nums)):
            result[i] = prefix[i] * suffix[i]
        
        return result