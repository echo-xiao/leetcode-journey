class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root
        
        while curr:
            if curr.left:
                predecessor = curr.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right