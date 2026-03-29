# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # If the current node is equal to p or q we know that is the LCA
        if root.val == p.val or root.val == q.val:
            return root
        
        # If the current node is greater than p or q and less than the other
        if (root.val > p.val and root.val < q.val) or (root.val < p.val and root.val > q.val):
            return root

        # If the current node is greater than both p and q
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # If the current node is less than both p and q
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)


