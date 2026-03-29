class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0
        left = right = 0

        # Split the string into each character
        split_s = list(s)

        # Iterate through the string
        while right < len(s):
            if split_s[right] in seen:

                # We need to move the left pointer to make the substring valid again
                while split_s[right] in seen:
                    # Remove the current character at the left pointer
                    seen.remove(split_s[left])

                    left += 1

                


            # Add the character to the seen set
            seen.add(split_s[right])

            right += 1

            # Check if we should update the max_length
            if (right - left) > max_len:
                max_len = right - left

            print(seen)
                

        return max_len