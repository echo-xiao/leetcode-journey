# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if head is None: return False
        if head.next is None: return True

        slow = head
        fast = head
        pre_slow = None

        # slow and fast pointers
        while fast is not None and fast.next is not None:
            pre_slow = slow
            slow = slow.next 
            fast = fast.next.next

        # break the link into two parts
        pre_slow.next = None
        if fast is not None:
            slow = slow.next

        # reverse link pre set up
        left = None

        # reverse link
        while slow is not None:
            right = slow.next
            slow.next = left
            left = slow
            slow = right


        # compare two link
        while left is not None and head is not None:
            if left.val == head.val:
                left = left.next
                head = head.next
            else:
                return False
        return True





