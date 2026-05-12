class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # First we can sort the input array
        nums.sort()

        # Keep a set of tuples to check what values we have already added
        seen = set()

        # Result array
        result = []

        # Start the 4 pointers process
        for i in range(0, len(nums) - 3):
            for j in range(i + 1, len(nums) -2):
                k = j + 1
                l = len(nums) - 1

                while k < l:
                    curr = nums[i] + nums[j] + nums[k] + nums[l]

                    if curr > target:
                        l -= 1
                    elif curr < target:
                        k += 1
                    else:
                        curr_nums = (nums[i],nums[j],nums[k],nums[l])
                        if curr_nums not in seen:
                            result.append([nums[i],nums[j],nums[k],nums[l]])
                            seen.add((nums[i],nums[j],nums[k],nums[l]))

                        k += 1
                        l -= 1

        return result