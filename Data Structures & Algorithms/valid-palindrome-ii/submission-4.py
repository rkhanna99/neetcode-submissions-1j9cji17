class Solution:
    def validPalindrome(self, s: str) -> bool:
        wrong = 0
        left = 0
        right = len(s) - 1

        while left < right:
            # Both characters are equal to each other
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            else:
                isPalindrome = (self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1))
                return isPalindrome

        return True

    # Helper function to check if a substring is a Palindrome
    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False

        return True