# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.isBalancedHelper(root)[0]
    
    def isBalancedHelper(self, root: Optional[TreeNode]) -> [bool, int]:
        if root is None:
            return [True, 0]

        left_height = self.isBalancedHelper(root.left)
        right_height = self.isBalancedHelper(root.right)

        balanced = left_height[0] and right_height[0] and (abs(left_height[1] - right_height[1]) <= 1)

        return [balanced, 1 + max(left_height[1], right_height[1])]