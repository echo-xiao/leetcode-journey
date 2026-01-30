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
        
        if root.val > target:
            direction = root.left
        else:
            direction = root.right

        res = self.closestValue(direction, target)

        if abs(target - res) > abs(root.val - target):
            return root.val
        elif abs(target - res) < abs(root.val - target):
            return res
        else:
            return min(res, root.val)
        

