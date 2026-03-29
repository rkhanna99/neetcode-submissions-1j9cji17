# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Set some base cases up
        if len(lists) == 0:
            return
        elif len(lists) == 1:
            return lists[0]
        else:
            # Start the process for merging the lists
            # We will treat the list as a stack
            while len(lists) != 1:
                l1 = lists.pop()
                l2 = lists.pop()
                merged_list = self.merge2Lists(l1, l2)
                lists.append(merged_list)
        
        return lists[0]
            
        

        
    def merge2Lists(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        # Initialize a dummy node to have a reference to the beginning of the list
        dummy = ListNode(-1)
        curr = dummy

        # Start iterating through both lists
        pointer1, pointer2 = l1, l2
        while pointer1 is not None and pointer2 is not None:
            # Check the values
            if pointer1.val >= pointer2.val:
                curr.next = pointer2
                pointer2 = pointer2.next
            else:
                curr.next = pointer1
                pointer1 = pointer1.next
            # Move our current pointer
            curr = curr.next

        # Check if there are any nodes remaining in l1 or l2
        if pointer1 is not None:
            curr.next = pointer1
        else:
            curr.next = pointer2

        return dummy.next
