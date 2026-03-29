# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    result = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.dfs(root)

        return self.result

    def dfs(self, curr: Optional[TreeNode]) -> int:
        if curr is None:
            return 0
        else:
            # Get the height of the left and right subtrees
            left = self.dfs(curr.left)
            right = self.dfs(curr.right)

            self.result = max(self.result, left + right)
            return 1 + max(left, right)
