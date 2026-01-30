class Solution:
    def __init__(self):
        self.prev = ListNode(0) 

        
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return None

        self.flatten(root.left)
        self.flatten(root.right)

        if root.left:
            oldRight = root.right
            root.right = root.left
            root.left = None

            curr = root
            while curr.right:
                curr = curr.right
            curr.right = oldRight

        ## 前序遍历 + 原地修改