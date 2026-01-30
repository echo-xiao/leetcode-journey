# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        curr = head
        cnt = 1
        while curr.next is not None:
            cnt += 1
            curr = curr.next
        curr.next = head

        r = k % cnt
        prev = ListNode(0)
        prev.next = head

        l = cnt-r

        while l > 0:
            prev = prev.next
            head = head.next
            l -= 1
        prev.next = None

        return head


