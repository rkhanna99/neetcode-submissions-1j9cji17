class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Get the frquency of each character in t
        t_dict = {}
        for c in list(t):
            if c not in t_dict:
                t_dict[c] = 1
            else:
                t_dict[c] += 1

        # Split the string s
        s_arr = list(s)

        # Initialize a return string
        ret, retLength = [-1, -1], float("infinity")

        have = 0
        need = len(t_dict)

        # Initilaize the left pointer and window dictionary
        left = 0
        window_dict = {}
        for right in range(len(s)):
            curr = s_arr[right]
            window_dict[curr] = 1 + window_dict.get(curr, 0)

            if curr in t_dict and window_dict[curr] == t_dict[curr]:
                have += 1
            
            # Start moving the left pointer if we have the needed unique characters
            while have == need:
                # Check if we need to update our result
                if right - left + 1 < retLength:
                    ret = [left, right]
                    retLength = right - left + 1
                
                # Move the left pointer but make window dict adjustment
                window_dict[s_arr[left]] = window_dict[s_arr[left]] - 1

                # Check if the removed character was even in t and adjust the have if needed
                if s_arr[left] in t_dict and window_dict[s_arr[left]] < t_dict[s_arr[left]]:
                    have = have - 1

                left += 1
        left, right = ret        
        return s[left:right + 1] if retLength != float("infinity") else ""
        
