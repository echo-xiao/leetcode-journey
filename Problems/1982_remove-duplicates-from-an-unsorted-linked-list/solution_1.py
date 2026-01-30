# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        dic = {}
        
        while curr is not None:
            if curr.val not in dic:
                dic[curr.val] = 1
            else:
                dic[curr.val] += 1
            curr = curr.next

        curr = head
        
        while curr is not None:
            if curr.val in dic and dic[curr.val] > 1:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next

        return dummy.next