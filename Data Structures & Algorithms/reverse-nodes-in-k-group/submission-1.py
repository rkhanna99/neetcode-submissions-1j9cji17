# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Get the length of the linked list
        list_len = 0
        curr = head
        while curr is not None:
            list_len += 1
            curr = curr.next

        # If the list_len >= k, we know there are groups to reverse
        if list_len >= k:
            # Dummy node to keep track of the head and manage connections
            dummy = ListNode(-1)
            dummy.next = head
            prev_group_end = dummy  # Tracks the end of the previous group

            while list_len >= k:
                # Set the start and end pointers for the current group
                pointer1 = prev_group_end.next
                pointer2 = self.traversekNodes(prev_group_end, k)

                # Save the start of the next group
                next_group_start = pointer2.next

                # Reverse the current group
                self.reverseNodes(pointer1, next_group_start)

                # Update connections
                prev_group_end.next = pointer2
                pointer1.next = next_group_start

                # Move prev_group_end to the end of the reversed group
                prev_group_end = pointer1

                # Reduce the remaining list length
                list_len -= k

            return dummy.next
        else:
            # If the list length is less than k, no reversal is needed
            return head
            
    # Helper function to reverse all the nodes from l1 to l2
    def reverseNodes(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> None:
        prev, curr = None, l1

        while curr != l2:
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        

    # Helper function that will traverse the linked list k times
    def traversekNodes(self, l1: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        while count != k:
            if l1 is None:
                return None
            else:
                l1 = l1.next
                count += 1
        return l1
        