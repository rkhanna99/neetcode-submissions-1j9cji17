class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        # List of Tuples [(str, {char : value})]
        char_tracker = []
        for s in strs:
            s_dict = {}
            if s == "":
                char_tracker.append([s, s_dict])
                continue
            else:
                for i in list(s):
                    if i in s_dict:
                        s_dict[i] = s_dict[i] + 1
                    else:
                        s_dict[i] = 1
            char_tracker.append([s, s_dict])

        print(char_tracker)

        # Use a dictionary to keep track of anagrams
        anagram_dict = {}

        for value in char_tracker:
            curr = frozenset(value[1].items())
            print(curr)
            if curr not in anagram_dict:
                anagram_dict[curr] = []
            anagram_dict[curr].append(value[0])
        
        return list(anagram_dict.values())




        