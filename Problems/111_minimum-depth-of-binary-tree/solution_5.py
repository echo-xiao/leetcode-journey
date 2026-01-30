# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
       if not root:
        return 0

       if root.left is None and root.right is None:
        return 1

       leftDepth = self.minDepth(root.left)
       rightDepth = self.minDepth(root.right)
       
       if root.left is None or root.right is None:
        return 1 + max(leftDepth, rightDepth)
        

       return min(leftDepth, rightDepth) + 1