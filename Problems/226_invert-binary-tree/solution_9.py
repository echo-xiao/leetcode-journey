class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # 1. 根节点先干活 (交换)
        root.left, root.right = root.right, root.left
        
        # 2. 再递归下去 (左右谁先谁后无所谓)
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root