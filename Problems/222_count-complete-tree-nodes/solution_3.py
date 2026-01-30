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

        left_depth = 0
        node = root.left
        while node:
            node = node.left
            left_depth += 1

        right_depth = 0
        node = root.right
        while node:
            node = node.left
            right_depth += 1
        
        if left_depth == right_depth:
            return 1 + (2 ** left_depth - 1) + self.countNodes(root.right)
        elif left_depth > right_depth:
            return 1 + self.countNodes(root.left) + (2 ** right_depth - 1)
            