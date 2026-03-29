# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        inOrderList = []
        self.kthSmallestHelper(root, inOrderList)
        return inOrderList[k - 1]


    def kthSmallestHelper(self, root: Optional[TreeNode], inOrderList):
        if root is None:
            return
        
        self.kthSmallestHelper(root.left, inOrderList)

        inOrderList.append(root.val)

        self.kthSmallestHelper(root.right, inOrderList)