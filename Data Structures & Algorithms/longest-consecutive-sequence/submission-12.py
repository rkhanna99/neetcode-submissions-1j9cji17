class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Base case
        if nums == []:
            return 0

        num_set = set(nums)
        print(num_set)
        seen = set()

        longest_sequence = -1
        curr_sequence = 1
        for num in nums:
            if (num - 1) not in num_set:
                print(num)
                seen.add(num)
                while num in num_set:
                    if ((num + 1) in num_set):
                        if ((num + 1) not in seen):
                            curr_sequence += 1
                            seen.add(num + 1)
                        num += 1
                    else:
                        break
                if curr_sequence >= longest_sequence:
                    longest_sequence = curr_sequence
                curr_sequence = 1
                print(seen)
                seen = set()

        return longest_sequence