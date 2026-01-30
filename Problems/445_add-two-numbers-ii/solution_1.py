# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = self.reverse(l1)
        curr2 = self.reverse(l2)

        dummy = ListNode(0)
        carry = 0

        while curr1 is not None or curr2 is not None or carry != 0:
            if curr1 is None: 
                v1 = 0
            else:
                v1 = curr1.val
            
            if curr2 is None: 
                v2 = 0
            else:
                v2 = curr2.val

            ttl = v1 + v2 + carry
            carry = ttl // 10
            val = ttl % 10

            curr = ListNode(val)
            curr.next = dummy.next
            dummy.next = curr

            if curr1 is not None: curr1 = curr1.next
            if curr2 is not None: curr2 = curr2.next

        return dummy.next
            
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr is not None:
            tmp = curr.next
            curr.next = prev
        
            prev = curr
            curr = tmp
    
        return prev
            
        