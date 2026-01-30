# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        return self.calcHeight(root) != -1

    def calcHeight(self, node: Optional[TreeNode]) -> int:

        if not node:
            return 0

        left_height = self.calcHeight(node.left)
        right_height = self.calcHeight(node.right)

        if abs(left_height - right_height) > 1 or left_height == -1 or right_height == -1:
            return -1
        
        return max(left_height, right_height) + 1