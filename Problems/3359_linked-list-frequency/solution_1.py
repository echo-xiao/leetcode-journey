# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def frequenciesOfElements(self, head):
        
        tmp = {}
        curr = head


        while curr is not None:
            if curr.val not in tmp:
                tmp[curr.val] = 1
            else:
                tmp[curr.val] += 1
            curr = curr.next

        dummy = ListNode(0)
        curr = dummy
        for i in tmp.values():
            new_node = ListNode(i)
            curr.next = new_node
            curr = curr.next
        return dummy.next

        