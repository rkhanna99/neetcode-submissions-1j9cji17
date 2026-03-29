# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Interate through the tree using BFS
        rightList = []

        queue = collections.deque()
        queue.append(root)

        while len(queue) > 0:
            total_elements = len(queue)
            # If there is only one element in the queue add it to the right list
            if total_elements == 1:
                curr_node = queue.popleft()
                if curr_node is not None:
                    # Add the children
                    queue.append(curr_node.left)
                    queue.append(curr_node.right)
                    rightList.append(curr_node.val)
            # More than one elements means we 
            elif total_elements > 1:
                count = 0
                changed = False
                while count != total_elements:
                    curr_node = queue.popleft()
                    if curr_node is not None:
                        queue.append(curr_node.left)
                        queue.append(curr_node.right)
                        # Keep changing the last node in right list
                        if changed == False:
                            rightList.append(curr_node.val)
                            changed = True
                        else:
                            rightList.pop()
                            rightList.append(curr_node.val)

                    count += 1

        return rightList
            

                    
             

        
        

