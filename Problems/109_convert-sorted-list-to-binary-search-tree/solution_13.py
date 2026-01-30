
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        size = 0
        ptr = head
        while ptr:
            size += 1
            ptr = ptr.next

        self.curr = head
        return self.buildTree(size)

    def buildTree(self, n: int) -> Optional[TreeNode]:
        if n <= 0:
            return None
        
        leftTree = self.buildTree(n//2)
        root = TreeNode(self.curr.val)
        root.left = leftTree
        
        self.curr = self.curr.next
        rightTree = self.buildTree(n-1-n//2)
        root.right = rightTree

        return root