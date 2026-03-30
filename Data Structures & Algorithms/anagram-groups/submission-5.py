class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_map = {}

        # Iterate through each string
        for s in strs:
            curr = list(s)
            curr_map = {}
            for c in curr:
                if c in curr_map:
                    curr_map[c] += 1
                else:
                    curr_map[c] = 1
            
            # Convert the curr_map to a frozenset to make the key hashable
            curr_frozenset = frozenset(curr_map.items())

            # Check if the current frozenset is in the char_map
            if curr_frozenset in char_map:
                char_map[curr_frozenset].append(s)
            else:
                char_map[curr_frozenset] = [s]

        print(char_map)

        result = []

        for key, value in char_map.items():
            result.append(value)

        return result

        