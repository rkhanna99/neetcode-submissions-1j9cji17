class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1

        while left < right:
            curr_left = s[left]
            curr_right = s[right]

            s[left] = curr_right
            s[right] = curr_left

            left += 1
            right -= 1