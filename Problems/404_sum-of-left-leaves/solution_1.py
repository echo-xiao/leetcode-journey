# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.res = 0
        self.traverse(root, None)
        return self.res

    def traverse(self, node: Optional[TreeNode], prev: Optional[TreeNode]):
        if not node:
            return 

        if node.left is None and node.right is None and prev is not None and prev.left == node:
            self.res += node.val

        self.traverse(node.left, node)
        self.traverse(node.right, node)