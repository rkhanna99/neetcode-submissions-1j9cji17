# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Check if there is another node after the intial one
        if head.next is None:
            return

        # Need to find the midpoint and endpoint of the list
        slow = fast = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Mark the midpoint and initialize a previes node
        midpoint = slow.next
        slow.next = prev = None

        # Reverse the nodes in the 2nd half
        while midpoint is not None:
            curr_next = midpoint.next
            midpoint.next = prev
            prev = midpoint
            midpoint = curr_next

        # Set pointers to head and end of list
        pointer1, pointer2 = head, prev
        while pointer2 is not None:
            temp1, temp2 = pointer1.next, pointer2.next
            pointer1.next = pointer2
            pointer2.next = temp1
            pointer1, pointer2 = temp1, temp2

        