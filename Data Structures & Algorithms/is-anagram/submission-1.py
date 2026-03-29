class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_split = list(s)
        t_split = list(t)

        print(s_split)
        print(t_split)

        # Check if the strings are a different length
        if len(s_split) != len(t_split):
            return False

        s_map = {}
        t_map = {}
        # Iterate through both strings at the same time
        for i in range(0, len(s_split)):
            # Handle s
            if s_split[i] not in s_map.keys():
                s_map[s_split[i]] = 1
            else:
                s_map[s_split[i]] += 1

            # Handle t
            if t_split[i] not in t_map.keys():
                t_map[t_split[i]] = 1
            else:
                t_map[t_split[i]] += 1

        print(s_map)
        print(t_map)

        return s_map == t_map