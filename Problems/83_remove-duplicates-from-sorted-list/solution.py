# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None 
            
        curr = head
        nxt = curr.next

        while curr is not None and nxt is not None:
            if curr.val == nxt.val:
                curr.next = nxt.next
                nxt = curr.next
            else:
                nxt = nxt.next
                curr = curr.next
        return head