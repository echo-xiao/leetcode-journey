# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0



        leftNodes = self.countNodes(root.left)
        rightNodes = self.countNodes(root.right)
    
        return leftNodes + rightNodes + 1