class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        # Start by adding every element to a set (we get O(1) runtime when checking if an element exists)
        num_set = set()
        for num in nums:
            if num in num_set:
                continue
            else:
                num_set.add(num)


        # Get every possible start to a sequence (n - 1 does not exist)
        start = []
        for num in num_set:
            if (num - 1) not in num_set:
                start.append(num)

        longest_sequence = 1

        for num in start:
            curr_sequence = 1
            curr_value = num + 1
            while curr_value in num_set:
                curr_sequence += 1
                curr_value += 1

            if curr_sequence > longest_sequence:
                longest_sequence = curr_sequence

        return longest_sequence