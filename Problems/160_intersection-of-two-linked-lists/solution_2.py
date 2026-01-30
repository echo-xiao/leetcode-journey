# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
    
        ptr1 = headA
        ptr2 = headB

        while ptr1 != ptr2:

            if ptr1 is None:
                ptr1 = headB
            if ptr2 is None:
                ptr2 = headA
            
            if ptr1 == ptr2:
                return ptr1

            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        return ptr1
