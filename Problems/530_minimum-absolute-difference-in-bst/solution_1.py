# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 

        self.prev = float('inf')
        self.min_diff = float('inf')
        self.traverse(root)
        return self.min_diff



    def traverse(self, node: Optional[TreeNode]):

        if not node:
            return

        self.traverse(node.left)

        diff = abs(self.prev - node.val)
        if diff < self.min_diff:
            self.min_diff = diff
        self.prev = node.val

        self.traverse(node.right)
