class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Create 2 pointers (one at the start and one at the end)
        left, right = 0, len(s) - 1

        while left < right:
            # Move the left until it points to an alphanumeric value
            while s[left].isalnum() == False and left < right:
                left += 1

            # Move the right until it points to an alphanumeric value
            while s[right].isalnum() == False and left < right:
                right -= 1

            # print(f"{s[left]} {s[right]}")

            if s[left].lower() != s[right].lower():
                return False
            
            left += 1
            right -= 1

        return True

