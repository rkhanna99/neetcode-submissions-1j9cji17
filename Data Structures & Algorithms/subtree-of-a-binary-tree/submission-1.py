# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        
        if subRoot is None:
            return True

        if self.sameTrees(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    

    # Helper function to check if 2 trees are the same
    def sameTrees(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        
        if (p is None) or (q is None) or (p.val != q.val):
            return False

        return self.sameTrees(p.left, q.left) and self.sameTrees(p.right, q.right)