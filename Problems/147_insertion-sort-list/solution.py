# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(0)
        dummy.next = head
        
        curr = head.next
        lastSorted = head

        while curr is not None:
            if curr.val > lastSorted.val:
                lastSorted = lastSorted.next
            else:
                prev = dummy
                while prev.next.val < curr.val:
                    prev = prev.next
                    
                lastSorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
            
            curr = lastSorted.next

        return dummy.next

