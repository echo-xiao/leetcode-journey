# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.traverse(root)
        return self.res

    def traverse(self, node: Optional[TreeNode]):
        if not node:
            return

        self.traverse(node.left)
        self.res.append(node.val)
        self.traverse(node.right)
    
        
