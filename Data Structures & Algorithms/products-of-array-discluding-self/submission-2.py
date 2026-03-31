class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Multiply everything and track the number of zeros
        product = 1
        zero_count = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zero_count += 1

        # Build the return array
        result = []
        if zero_count > 1:
            return [0 for i in range(len(nums))]
        elif zero_count == 1:
            for num in nums:
                if num == 0:
                    result.append(product)
                else:
                    result.append(0)
            return result
        else:
            # There are no zeros
            for num in nums:
                result.append(product // num)
            
            return result

            