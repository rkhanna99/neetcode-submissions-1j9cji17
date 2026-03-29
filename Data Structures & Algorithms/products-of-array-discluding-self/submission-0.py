class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_tracker = []

        # Calculate the product without any zeros
        for i in range(0, len(nums)):
            if nums[i] != 0:
                product = product * nums[i]
            else:
                zero_tracker.append(i)

        return_list = []
        # Check if our zero tracker is empty
        if len(zero_tracker) == 0:
            for num in nums:
                return_list.append(product // num)
            return return_list
        elif len(zero_tracker) == 1:
            for i in range(0, len(nums)):
                if nums[i] != 0:
                    nums[i] = 0
                else:
                    nums[i] = product
            return nums
        else:
            for num in nums:
                return_list.append(0)
            return return_list
        
