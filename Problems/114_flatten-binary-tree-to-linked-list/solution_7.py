class Solution:
    def __init__(self):
        self.prev = ListNode(0) 

        
    def flatten(self, root: Optional[TreeNode]) -> None:
   
        return self.dfs(root)

    def dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        leftTail = self.dfs(root.left)
        rightTail = self.dfs(root.right)

        if root.left is not None:
            leftTail.right = root.right
            root.right = root.left
            root.left = None

        return rightTail or leftTail or root
        
