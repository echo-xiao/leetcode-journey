class Solution(object):
    def reverseList(self, head):

        if head is None:
            return head

        left = None
        right = head

        while right.next is not None:
            helper = right.next
            right.next = left

            left = right
            right = helper

        head = right
        head.next = left 
        return head
