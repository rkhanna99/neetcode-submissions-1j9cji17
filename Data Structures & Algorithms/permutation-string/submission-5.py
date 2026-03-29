class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Base cases
        if len(s1) > len(s2):
            return False

        # Map all of the characters in s1
        s1_map = {}
        for c in list(s1):
            if c in s1_map:
                s1_map[c] += 1
            else:
                s1_map[c] = 1

        # Set up left and right pointers for our sliding window on s2
        left = right = 0

        # Set up a map to track the characters in the sliding window of s2
        s2_map = {}

        # Move the right pointer initially to match the length of s1
        split_s2 = list(s2)
        while right < len(s1):
            if split_s2[right] in s2_map:
                s2_map[split_s2[right]] += 1
            else:
                s2_map[split_s2[right]] = 1

            right += 1

        
        # Check if the maps match otherwise just slide the window
        while right <= len(s2):
            print(right)
            # Remove any keys with value 0 in the s2 map
            s2_map = {key: value for key, value in s2_map.items() if value != 0}
            print(s2_map)

            if s1_map == s2_map:
                return True
            else:
                if right == len(s2):
                    break
                # Move the pointers and then update the s2 dictionary accordingly

                # Right pointer
                if split_s2[right] in s2_map:
                    s2_map[split_s2[right]] += 1
                else:
                    s2_map[split_s2[right]] = 1

                right += 1

                # Left pointer
                s2_map[split_s2[left]] -= 1
                left += 1




        return False