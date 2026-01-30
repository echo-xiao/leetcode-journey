# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        diff = float('inf')
        prev = None
        min_diff = float('inf')

        if not root: 
            return



        def traverse(node: Optional[TreeNode]):
            if not node:
                return 

            nonlocal diff, prev, min_diff

            traverse(node.left)

            if prev is not None:
                diff = abs(prev - node.val)
                min_diff = min(min_diff, diff)

            prev = node.val
            
            traverse(node.right)

        traverse(root)
        return min_diff
