# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # We will do a BFS traveral
        result = []

        # Create a queue and add the root
        queue = collections.deque()
        queue.append(root)

        # Iterate till the queue is empty
        while len(queue) > 0:
            # Length of the queue will let us know how many nodes on curr level
            queue_length = len(queue)
            curr_level = []
            for i in range(queue_length):
                curr_node = queue.popleft()
                
                # Ensure that the current node is not none
                if curr_node is not None:
                    queue.append(curr_node.left)
                    queue.append(curr_node.right)
                    curr_level.append(curr_node.val)
            
            if len(curr_level) > 0:
                result.append(curr_level)

        return result
