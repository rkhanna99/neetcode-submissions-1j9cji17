class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        max_len = 0

        split_s = list(s)

        seen = {}
        while right < len(s):

            # Add the right character to the seen map
            if split_s[right] in seen:
                    seen[split_s[right]] += 1
            else:
                seen[split_s[right]] = 1

            max_key = max(seen, key=seen.get)
            max_count = seen[max_key]

            right += 1
            
            # Check if the current window is valid and move if the current window size - count of max character is greater than the replacements allowed
            while right - left - max_count > k:
                seen[split_s[left]] -= 1
                left += 1
           

                

            # Update the max length if needed
            if right - left > max_len:
                max_len = right - left
            
            print(seen)

        return max_len
