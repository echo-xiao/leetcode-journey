# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        
        if not head.next:
            return TreeNode(head.val)

        mid = self.findMiddleAndCut(head)
        root = TreeNode(mid.val)

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)

        return root

    def findMiddleAndCut(self, head: Optional[ListNode]) -> ListNode:
        fast = head
        slow = head
        prev = None

        while fast is not None and fast.next is not None:
            prev = slow
            fast = fast.next.next
            slow = slow.next

        if prev is not None:
            prev.next = None
        return slow