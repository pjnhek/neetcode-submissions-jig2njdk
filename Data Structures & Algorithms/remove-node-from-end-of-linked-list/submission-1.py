# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # use two pointers, first create new ListNode that starts at 0 and next is head
        # we do this because we want to point left to the start of that and right to head
        # without doing so, the incrementation will be wrong, for ex. n = 2 will make left 
        # pointer land on the value that needs to be removed instead of the prev value 
        # we need left to be on prev val and then point next to next.next to skip removed val
        dummy = ListNode(0, head)
        left = dummy
        right = head
        # increment between left and right, n space between them
        while n > 0:
            right = right.next
            n -= 1
        # move left and right at same pace until right is None, once that point is reached, we know that
        # we need to skip left.next and replace it with left.next.next
        while right:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
        
        