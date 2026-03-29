class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ret_dict = {}
        for i in nums:
            if i not in ret_dict:
                ret_dict[i] = 1
            else:
                return True
        return False  