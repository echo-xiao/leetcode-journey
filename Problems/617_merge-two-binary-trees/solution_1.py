# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        return self.traverse(root1, root2)
        

    def traverse(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not p:
            return q
        if not q:
            return p
        
        p.val = p.val + q.val
        p.left = self.traverse(p.left, q.left)
        p.right = self.traverse(p.right, q.right)

        return p