# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        if not root:
            return 0

        midVal = 0
        leftSum = self.rangeSumBST(root.left, low, high)
        
        if root.val <= high and root.val >= low:
            midVal += root.val

        rightSum = self.rangeSumBST(root.right, low, high)

        return leftSum + rightSum + midVal
