class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        for c in list(s1):
            if c not in s1_dict:
                s1_dict[c] = 1
            else:
                s1_dict[c] = s1_dict[c] + 1
        print(s1_dict)

        # Initialize the left, right pointers for the sliding window
        left = right = 0

        # Split the s2 string
        s2_list = list(s2)

        while right < len(s2_list):
            # If the current character is not in s1 we can ignore it
            if s2_list[right] not in s1_dict:
                right = right + 1
                continue
            else:
                left = curr = right
                right = right + len(s1)
                if right > len(s2_list):
                    return False
                temp = {}
                while left != right:
                    if s2_list[left] not in temp:
                        temp[s2_list[left]] = 1
                    else:
                        temp[s2_list[left]] = temp[s2_list[left]] + 1
                    left = left + 1
                print(temp)
                if temp == s1_dict:
                    return True
                else:
                    right = curr + 1
                    continue

        return False
