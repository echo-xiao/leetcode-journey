# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.res = 0
        self.low = low
        self.high = high
        self.traverse(root)
        
        return self.res

    def traverse(self, node: Optional[TreeNode]) -> int:
        
        if not node:
            return 0

        self.traverse(node.left)
        
        if node.val <= self.high and node.val >= self.low:
            self.res += node.val

        self.traverse(node.right)

