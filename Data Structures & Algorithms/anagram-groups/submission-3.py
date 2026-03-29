class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}

        # Iterate through each value in strs
        for value in strs:
            curr_dict = self.charHelper(value)
            curr_key = frozenset(curr_dict.items())

            if curr_key not in anagram_dict.keys():
                anagram_dict[curr_key] = [value]
            else:
                anagram_dict[curr_key].append(value)

        ret_list = []
        for key, value in anagram_dict.items():
            ret_list.append(value)

        return ret_list



    # Helper method that will take a string and return a dictionary which counts the frequency of each character
    def charHelper(self, value: str) -> {}:
        ret_dict = {}
        value_split = list(value)
        for c in value_split:
            if c not in ret_dict.keys():
                ret_dict[c] = 1
            else:
                ret_dict[c] += 1

        return ret_dict