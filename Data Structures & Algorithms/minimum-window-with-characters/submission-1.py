class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Handle some base cases (t == s and t is longer than s)
        if len(t) > len(s):
            return ""
        elif t == s:
            return t
        else:
            # Create a dictionary to keep track of the frequency of each character in t
            t_map = {}
            for c in list(t):
                if c in t_map:
                    t_map[c] += 1
                else:
                    t_map[c] = 1

            # Set up the sliding window to move through s in O(n) time
            left = right = 0
            s_map = {}

            # Save the indicies for the minimum string
            min_left = min_right = 0
            min_length = float('inf')

            # Instead of checking s_map on each iteration we can just increment/decrement a value to indicate if we have a valid string
            satisfied_count, needed = 0, len(t_map)

            # Start moving through s
            while right < len(s):
                # Move the right pointer if we don't have a valid string
                if s[right] in s_map:
                    s_map[s[right]] += 1
                else:
                    s_map[s[right]] = 1

                # Check if we have satisfied a character count (Exactly equal)
                if s[right] in t_map:
                    if s_map[s[right]] == t_map[s[right]]:
                        satisfied_count += 1
                
                # Move the right pointer
                right += 1

                # Check if we have currently have a valid string (move the left pointer)
                while satisfied_count == needed:
                    # Check if this current string is shorter than the one that we saved
                    if right - left < min_length:
                        min_left = left
                        min_right = right
                        min_length = right - left

                    # Remove the current left character from the s_map (We know this exists in the map cause the right would have already added it)
                    s_map[s[left]] -= 1
                    # Check if the count is still valid (We have at least as many s[left] characters left in the window)
                    if s[left] in t_map:
                        if s_map[s[left]] < t_map[s[left]]:
                            satisfied_count -= 1
                    # Move the left pointer
                    left += 1

            return s[min_left:min_right]





