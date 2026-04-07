class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Alpabetic
        strs.sort()

        ret_string = ""

        # Iterate through each character
        for i in range(0, len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                ret_string += (strs[0][i]) 
            else:
                break

        return ret_string