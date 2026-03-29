class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(len(nums)):
            num_dict[i] = nums[i]

        print(num_dict)
        for j in num_dict:
            val_needed = target - num_dict[j]
            key_needed = [key for key, value in num_dict.items() if value == val_needed and key is not j] 
            if len(key_needed) > 0:
                return [j, key_needed[0]]
        
        return [0, 0]