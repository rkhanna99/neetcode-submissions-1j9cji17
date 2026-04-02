class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for i in range(0, len(nums))]
        # Need to calculte the prefix product
        running_prefix_product = 1
        for i in range(1, len(nums)):
            prefix[i] = nums[i - 1] * running_prefix_product
            running_prefix_product = prefix[i]
        
        # Calculate the suffix product (start at the 2nd to last value)
        suffix = [1 for i in range(0, len(nums))]
        running_suffix_product = 1
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = nums[i + 1] * running_suffix_product
            running_suffix_product = suffix[i]

        result = []
        for i in range(0, len(nums)):
            result.append(prefix[i] * suffix[i])

        return result


        # [1,1,2,8]
        # [48,24,6,1]