# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        if not root.left:
            return root.val == 1
    
        leftCheck = self.evaluateTree(root.left)
        rightCheck = self.evaluateTree(root.right)

        if root.val == 2:
            return leftCheck or rightCheck
        elif root.val == 3:
            return leftCheck and rightCheck
