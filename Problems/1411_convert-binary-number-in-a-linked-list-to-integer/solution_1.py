# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        
        total_value = 0
        curr = head

        while curr is not None:
            total_value = total_value * 2 + curr.val
            curr = curr.next
        return total_value