# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        # Invert the current node
        self.invertTreeHelper(root)

        # Recursively move the current node
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
    
    # Invert one node
    def invertTreeHelper(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        curr_left = root.left
        curr_right = root.right
        root.left = curr_right
        root.right = curr_left 