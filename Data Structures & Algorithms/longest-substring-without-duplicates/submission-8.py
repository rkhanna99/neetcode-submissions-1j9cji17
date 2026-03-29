class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_substring_length = 0
        
        input_list = list(s)

        curr_longest_set = set()
        for character in input_list:
            if character not in curr_longest_set:
                curr_longest_set.add(character)
                if len(curr_longest_set) > longest_substring_length:
                    longest_substring_length = len(curr_longest_set)
                continue
            else:
                # Reset the current longest set as we have found a duplicate
                if input_list[-1] not in curr_longest_set:
                    curr_longest_set.add(character)
                else:
                    curr_longest_set = set()
        
        return longest_substring_length
            