# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # We want to iterate through both lists at the same time and create a list to return
        dummy = ListNode(-1)
        new_list = dummy

        # Start iterating through the list and initialize a carry
        carry = 0
        while l1 is not None or l2 is not None:
            # Add the digits up and account for uneven lengths
            if l1 is None:
                curr_val = l2.val + carry
            elif l2 is None:
                curr_val = l1.val + carry
            else:
                curr_val = l1.val + l2.val + carry
            
            # Check if the added value is more than 1 digit
            carry = curr_val // 10
            new_val = curr_val % 10
            
            new_list.next = ListNode(new_val)
            new_list = new_list.next

            # Move the pointers
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        # Edge case if we reach the end and still have a carry
        if carry != 0:
            new_list.next = ListNode(carry)
        
        return dummy.next
            

