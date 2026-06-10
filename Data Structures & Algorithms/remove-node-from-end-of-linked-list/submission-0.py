# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use two pointers, first pointer is the start, second pointer is n increments from first
        # loop until second pointer is None
        # first pointer is now on the node that needs to be removed
        dummy = ListNode(0, head)
        left = dummy
        right = head
        while n > 0:
            n -= 1
            right = right.next
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
        
        