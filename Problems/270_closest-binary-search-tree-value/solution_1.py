# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        if not root:
            return float('inf')

        if target == root.val:
            return root.val
        elif target > root.val:
            closest = self.closestValue(root.right, target)
        elif target < root.val:
            closest = self.closestValue(root.left, target)

        if abs(target - root.val) == abs(target - closest):
            return min(root.val, closest)
        elif abs(target - root.val) < abs(target - closest):
            return root.val
        elif abs(target - root.val) > abs(target - closest):
            return closest


        