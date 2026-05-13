class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize a value to track the longest substring
        longest = 0

        # Initialize a left pointer
        left = 0

        # Use a set to keep track of elements in a window
        window = set()

        # Start moving the right pointer
        for right in range(len(s)):
            # Check if the current character is in the window
            if s[right] not in window:
                window.add(s[right])
            else:
                while s[right] in window:
                    window.remove(s[left])
                    left += 1

                window.add(s[right])

            # Check if the current window length is the largest we have seen
            if right - left + 1 > longest:
                longest = right - left + 1

        return longest     