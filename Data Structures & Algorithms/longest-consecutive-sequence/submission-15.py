class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = 0
        num_set = set()

        # Add each value to the set
        for num in nums:
            num_set.add(num)

        # Check every value in the set to see if the value can be the beginning of a sequence
        beginning = []
        for num in num_set:
            target = num - 1
            if target in num_set:
                continue
            else:
                beginning.append(num)

        # Now that we have every value that can start a sequence we loop through those to see which starts the longest
        for i in range(0, len(beginning)):
            curr_sequence = 0
            curr_value = beginning[i]

            while curr_value in num_set:
                curr_sequence += 1
                curr_value += 1
            
            if curr_sequence > longest_sequence:
                longest_sequence = curr_sequence

        return longest_sequence