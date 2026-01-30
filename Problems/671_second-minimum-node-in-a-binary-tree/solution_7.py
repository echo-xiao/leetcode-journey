# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        self.min_res = float('inf')

        self.targetVal = root.val
        self.traverse(root)

        if self.min_res == float('inf'):
            return -1
        else:
            return self.min_res


    def traverse(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 

        self.traverse(node.left)
        self.traverse(node.right)

        if node.val > self.targetVal:
            self.min_res = min(self.min_res, node.val)

