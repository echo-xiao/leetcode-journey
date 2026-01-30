# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        targetVal = root.val

        return self.check(root, targetVal)

    def check(self, node: Optional[TreeNode], targetVal: int) -> bool:

        if not node:
            return True

        leftCheck = self.check(node.left, targetVal)
        rightCheck = self.check(node.right, targetVal)
        midCheck = (node.val == targetVal)

        return leftCheck and rightCheck and midCheck


    