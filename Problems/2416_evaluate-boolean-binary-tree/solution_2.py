# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        res = self.traverse(root)
        if res == 1:
            return True
        elif res == 0:
            return False

    def traverse(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 

        if node.val < 2:
            return node.val == 1

        leftCheck = self.traverse(node.left)
        rightCheck = self.traverse(node.right)

        if node.val == 2:
            return leftCheck or rightCheck
        elif node.val == 3:
            return leftCheck and rightCheck


