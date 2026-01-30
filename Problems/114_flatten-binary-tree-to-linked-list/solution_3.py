class Solution:
    def __init__(self):
        self.prev = ListNode(0) 

        
    def flatten(self, root: Optional[TreeNode]) -> None:
   
        return self.dfs(root)

    def dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        left = self.dfs(root.left)
        right = self.dfs(root.right)

        root.left = None
        root.right = left

        curr = root
        while curr.right:
            curr = curr.right

        curr.right = right

        return root
        
        