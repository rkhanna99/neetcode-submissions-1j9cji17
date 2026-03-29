"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # First we will create a map of every current node to a copy
        # map[curr_node] = new_node
        node_dict = {None: None}
        pointer = head
        while pointer is not None:
            copy_node = Node(pointer.val)
            node_dict[pointer] = copy_node
            pointer = pointer.next

        # Initialize a dummy node to save reference to beginning
        dummy = Node(-1)
        pointer = head
        dummy.next = pointer

        # We can just iterate through the list again and use the map to set references
        while pointer is not None:
            # Get the current node
            curr_copy_node = node_dict[pointer]
            curr_copy_node.next = node_dict[pointer.next]
            curr_copy_node.random = node_dict[pointer.random]
            pointer = pointer.next
        
        return node_dict[head]
            