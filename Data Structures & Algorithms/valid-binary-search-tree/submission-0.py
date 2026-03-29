# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, -1001, 1001)

    # Check if one node is valid in the Binary search tree
    def isValidBSTHelper(self, root: Optional[TreeNode], minimum: int, maximum: int) -> bool:
        if root is None:
            return True
        
        if not (minimum < root.val < maximum):
            return False

        return (self.isValidBSTHelper(root.left, minimum, root.val) and self.isValidBSTHelper(root.right, root.val, maximum))
        
        