class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum = 0
        prefix_map = {0:1}
        result = 0

        for i in range(0, len(nums)):
            running_sum += nums[i]
            target_prefix = running_sum - k
            if target_prefix in prefix_map:
                result += prefix_map[target_prefix]
            
            if running_sum in prefix_map:
                prefix_map[running_sum] += 1
            else:
                prefix_map[running_sum] = 1

        return result
                
