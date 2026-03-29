class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        # Sort the array O(n log n)
        nums.sort()

        for i in range(0, len(nums)):
            # Continue if we have duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Set our 2 pointers
            left, right = i + 1, len(nums) - 1
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                if curr == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    # Move ahead for duplicates for our two pointers
                    while left < right and nums[left] == nums[left + 1]:
                        left = left + 1
                    while left < right and nums[right] == nums[right - 1]:
                        right = right - 1
                    # Increment the pointers
                    left = left + 1
                    right = right - 1
                elif curr > 0:
                    right = right - 1
                elif curr < 0:
                    left = left + 1
        return triplets