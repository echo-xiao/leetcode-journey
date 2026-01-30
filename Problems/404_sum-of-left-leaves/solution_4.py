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

        leftVal = 0

        if root.left and root.left.left is None and root.left.right is None:
            leftVal = root.left.val

        leftSum = self.sumOfLeftLeaves(root.left)
        rightSum = self.sumOfLeftLeaves(root.right)

        return leftVal + leftSum + rightSum