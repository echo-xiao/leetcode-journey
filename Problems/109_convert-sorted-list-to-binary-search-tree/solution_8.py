
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if head is None:
            return None

        if head.next is None:
            return TreeNode(head.val)

        slow, fast = head, head
        prev = None

        while fast is not None and fast.next is not None:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        
        if prev is not None:
            prev.next = None

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)

        return root