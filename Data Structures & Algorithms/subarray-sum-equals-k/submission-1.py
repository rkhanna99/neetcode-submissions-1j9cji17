class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        running_sum = 0
        prefix_map = {0:1}
        count = 0

        for i in range(0, len(nums)):
            running_sum += nums[i]
            complement = running_sum - k

            if complement in prefix_map:
                count += prefix_map[complement]

            if running_sum in prefix_map:
                prefix_map[running_sum] += 1
            else:
                prefix_map[running_sum] = 1

        return count
            
            