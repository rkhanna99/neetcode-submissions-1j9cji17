class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []


        ret_list = []
        seen = set()
        # Iterate through the nums using 3 pointers
        for i in range(0, len(nums) - 2):
            for j in range(1, len(nums) - 1):
                for k in range(2, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        if frozenset([nums[i], nums[j], nums[k]]) in seen:
                            continue
                        elif (i == j or i == k or j == k):
                            continue
                        else:
                            print(f"nums[i] = {nums[i]}")
                            print(f"nums[j] = {nums[j]}")
                            print(f"nums[k] = {nums[k]}")
                            ret_list.append([nums[i], nums[j], nums[k]])
                            seen.add(frozenset([nums[i], nums[j], nums[k]]))
        return ret_list