
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        size = 0
        ptr = head
        while ptr is not None:
            size += 1
            ptr = ptr.next

        self.curr = head
        return self.build(0, size-1)

    def build(self, left: int, right: int) -> Optional[TreeNode]:
        
        if left > right:
            return None

        mid = (left + right) // 2
        leftTree = self.build(left, mid-1)
        root = TreeNode(self.curr.val)
        root.left = leftTree
        self.curr = self.curr.next
        root.right = self.build(mid+1, right)

        return root