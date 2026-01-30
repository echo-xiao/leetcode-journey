# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteNodes(self, head, m, n):
        
        if head is None: return head
        
        dummy = ListNode(0)
        dummy.next = head

        curr = dummy

        while curr is not None:

            slow = curr

            for _ in range(m):
                if slow is None:
                    break
                slow = slow.next

            if slow is None: break
            fast = slow.next

            for _ in range(n):
                if fast is None:
                    break
                fast = fast.next
            
            slow.next = fast
            curr = slow

        return head
