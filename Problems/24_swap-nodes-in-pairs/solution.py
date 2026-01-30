# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

            
        dummy = ListNode(0)
        dummy.next = head
        first = head
        second = head.next
        prev = dummy
        

        while second is not None:
            nxt = second.next
            second.next = first
            first.next = nxt
            prev.next = second

            prev = first
            first = nxt
            if first is not None:
                second = first.next
            else:
                second = None
            
        return dummy.next