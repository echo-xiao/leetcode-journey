# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if head is None: return None
        if head.next is None: return head

        left = head
        right = left.next

        while right is not None:
            if left.val == right.val:
                right = right.next
                left.next = right
            else:
                right = right.next
                left = left.next

        return head
