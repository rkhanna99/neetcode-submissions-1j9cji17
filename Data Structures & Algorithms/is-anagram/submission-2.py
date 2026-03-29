class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)

        i = 0
        j = len(t_list) - 1

        # Base Case
        if len(s) != len(t):
            return False
        
        s_map = {}
        t_map = {}

        # Iterate through both at the same time
        for i in range(0, len(s)):
            curr_s = s_list[i]
            curr_t = t_list[i]
            
            # Check s
            if curr_s in s_map:
                s_map[curr_s] += 1
            else:
                s_map[curr_s] = 1

            # Check t
            if curr_t in t_map:
                t_map[curr_t] += 1
            else:
                t_map[curr_t] = 1

        return s_map == t_map
