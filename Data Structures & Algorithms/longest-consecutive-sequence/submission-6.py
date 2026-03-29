class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        # Convert the array to a set to avoid duplicates
        num_set = set(nums)
        print(num_set)

        longest_sequence = 0
        for num in num_set:
            # Start a new sequence only if `num - 1` is not in the set
            if (num - 1) not in num_set:
                current_num = num
                current_sequence = 1

                # Count consecutive numbers
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_sequence += 1

                # Update the longest sequence found
                longest_sequence = max(longest_sequence, current_sequence)

        return longest_sequence