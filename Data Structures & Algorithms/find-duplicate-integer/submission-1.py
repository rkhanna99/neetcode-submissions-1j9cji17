class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Use a slow and fast pointer and move through the array as if it were a list
        slow, fast = 0, 0

        # Find the intersection point of the slow and fast pointers
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Now we will use a 2nd slow pointer to find the intersection between that and the original slow pointer
        slow2 = 0

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
            
        return slow
