# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        # We will use BFS to traverse the tree
        queue = collections.deque()
        right_visible = []

        queue.append(root)

        # Start the traversal
        while len(queue) > 0:
            # We want to append the last node on every left that we've traversed
            queue_len = len(queue)

            if queue_len == 1:
                # Check if the one node is none
                curr = queue.popleft()
                if curr is not None:
                    queue.append(curr.left)
                    queue.append(curr.right)
                right_visible.append(curr.val)
            else:
                # More than one node in the queue
                changed = False
                for i in range(queue_len):
                    curr = queue.popleft()
                    if curr is not None:
                        queue.append(curr.left)
                        queue.append(curr.right)

                        if changed == False:
                            right_visible.append(curr.val)
                            changed = True
                        else:
                            right_visible.pop()
                            right_visible.append(curr.val)


        return right_visible
            