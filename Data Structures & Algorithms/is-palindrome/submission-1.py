class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = ""

        # Ensure the string is in the correct format
        for c in list(s):
            c = c.lower()
            if c.isalnum():
                cleaned_str += c

        # Split the string
        split_s = list(cleaned_str)

        # Set up a pointer at the beginning and the end of the string
        start_s = 0
        end_s = len(split_s) - 1

        # Move the 2 pointers until they are in an equal spot
        while start_s < end_s:
            if split_s[start_s] != split_s[end_s]:
                print(f"Start value: {split_s[start_s]}")
                print(f"End value: {split_s[end_s]}")
                return False
            else:
                start_s += 1
                end_s -= 1
            
        return True