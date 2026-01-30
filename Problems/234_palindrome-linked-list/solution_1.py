# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        stack = []

        curr = head
        while curr is not None:
            stack.append(curr.val)
            curr = curr.next
        
        tag = True
        curr = head
        while curr is not None:
            val = stack.pop()
            if val != curr.val:
                tag = False
                break
            curr = curr.next
        return tag

