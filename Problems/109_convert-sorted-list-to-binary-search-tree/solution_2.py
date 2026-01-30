
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        self.head = head
        return self.buildBST(0, size-1)

    def buildBST(self, left: int, right: int):
        if left > right:
            return None

        mid = left + (right - left) // 2
        
        leftTree = self.buildBST(left, mid-1)
        root = TreeNode(self.head.val)
        root.left = leftTree
        self.head = self.head.next
        root.right = self.buildBST(mid+1, right)

        return root