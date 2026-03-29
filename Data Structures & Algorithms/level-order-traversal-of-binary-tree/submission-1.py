# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # We will use BFS to do a level order traversal
        queue = collections.deque()
        queue.append(root)
        levels = []    
        
        # Start the traversal
        while len(queue) > 0:
            queue_length = len(queue)
            curr_level = []

            for i in range(queue_length):
                curr = queue.popleft()
                
                if curr is not None:
                    queue.append(curr.left)
                    queue.append(curr.right)
                    curr_level.append(curr.val)

            if len(curr_level) > 0:
                levels.append(curr_level)

        return levels