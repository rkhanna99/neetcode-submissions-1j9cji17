class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:

            # Check if both left and right are at alpha-numeric characters
            while s[left].isalnum() == False and left != (len(s) - 1):
                left += 1

            while s[right].isalnum() == False and right != 0:
                right -= 1

            if left < right:
                if s[left].lower() != s[right].lower():
                    return False

                left += 1
                right -= 1
            
        return True