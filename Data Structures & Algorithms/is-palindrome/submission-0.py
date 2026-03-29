class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_list = []
        for char in s.lower():
            if char.isalnum():
                str_list.append(char)

        i = 0
        j = len(str_list) - 1
        for count in range(0, len(str_list)):
            if i == j:
                break
            if str_list[i] == str_list[j]:
                i = i + 1
                j = j - 1
                continue
            else:
                return False
        return True