# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def gameResult(self, head):
        
        if head is None: return 'Tie'

        curr = head
        even = 0
        odd = 0

        while curr is not None and curr.next is not None:
            if curr.val > curr.next.val:
                even += 1
            elif curr.val < curr.next.val:
                odd += 1

            curr = curr.next.next

        if even > odd:
            return 'Even'
        elif even < odd:
            return 'Odd'
        else:
            return 'Tie'                
            
        