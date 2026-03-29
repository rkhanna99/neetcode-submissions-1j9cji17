# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Base case if head.next = None
        if head.next is None:
            if n == 1:
                return head.next
            else:
                return head

        # Create a dummy node and set the next to head
        dummy = ListNode(-1)
        dummy.next = head

        # Initialize a slow and fast pointer
        slow, fast = dummy, head

        # Start out by moving the fast pointer n times ahead
        count = 1
        while count != n:
            fast = fast.next
            count += 1
        
        # Now we move the pointer together by one until we get fast to the end
        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        # We now know fast is at the end and slow is right before the node we need to delete
        slow.next = slow.next.next

        return dummy.next