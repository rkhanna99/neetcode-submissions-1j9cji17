# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head.next is None:
            return False
        slow = head
        fast = head
        while slow is not None and fast is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
