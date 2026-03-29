# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfsHelper(root, root.val)

    def dfsHelper(self, root: TreeNode, max_so_far: int) -> int:
        if root is None:
            return 0
        elif root.val >= max_so_far:
            count = 1
        else:
            count = 0
            
        max_so_far = max(root.val, max_so_far)

        count += self.dfsHelper(root.left, max_so_far)
        count += self.dfsHelper(root.right, max_so_far)

        return count