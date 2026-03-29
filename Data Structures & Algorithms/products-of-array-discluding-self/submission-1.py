class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ret_list = []
        
        total = 1
        zero_count = 0
        # Iterate through each value in nums and multiply the values together unless we encounter a 0
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                total = total * num

        # Base case if we have more than 1 zero (Everything is 0)
        if zero_count > 1:
            return ([0] * len(nums))

        # After getting the total we can iterate through the list and divide each number by the total unless we encounter a 0
        for num in nums:
            if num == 0:
                ret_list.append(total)
            elif zero_count > 0:
                ret_list.append(0)
            else:
                ret_list.append(int(total/num))

        return ret_list