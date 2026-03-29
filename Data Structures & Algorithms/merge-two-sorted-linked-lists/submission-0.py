# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node
        dummy = ListNode(-1)
        tail = dummy

        # Start iterating through both lists
        while list1 is not None and list2 is not None:
            if list1.val >= list2.val:
                tail.next = list2
                list2 = list2.next
            else:
                tail.next = list1
                list1 = list1.next
            
            tail = tail.next
        
        # We will have some values left in either l1 or l2 so we must append
        if list1 is None:
            tail.next = list2
        else:
            tail.next = list1

        # Return reference to the new lists head
        return dummy.next

