# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head

        fast, slow = head.next, head

        while fast is not None and fast.next is not None:
            fast =  fast.next.next
            slow = slow.next
        
        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.mergeTwoSortedList(left, right)

    def mergeTwoSortedList(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy

        while left is not None and right is not None:
            if left.val < right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        if left is not None:
            curr.next = left
        elif right is not None:
            curr.next = right

        return dummy.next















    
        