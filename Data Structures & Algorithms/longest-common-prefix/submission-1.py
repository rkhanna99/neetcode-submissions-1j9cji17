class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Initialize a return value
        common = ""

        # Sort the strs array
        strs.sort()

        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] == strs[-1][i]:
                common += strs[0][i]
            else:
                break
        
        return common

        
