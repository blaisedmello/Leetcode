# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse_linkedlist(h, c):
            start = h
            prev = None
            while start and c <= right:
                temp = start.next
                start.next = prev
                prev = start
                start = temp
                c += 1
            h.next = start
            return prev
        
        curr = head
        prev = None
        count = 1
        while count < left:
            prev = curr
            curr = curr.next
            count += 1
        l = reverse_linkedlist(curr, count)
        if left == 1:
            return l
        prev.next = l
        return head