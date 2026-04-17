class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Create the pointers for our window
        left = 0

        # Initialize a set to keep track of the numbers in the window
        num_set = set()
        for right in range(0, len(nums)):
            # Move the left side of the window
            if right - left > k:
                curr_left = nums[left]
                num_set.remove(curr_left)
                left += 1
            
            # Check if the right value is in the window
            if nums[right] in num_set:
                return True

            num_set.add(nums[right])

        return False 