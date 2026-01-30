# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        return self.dfs(root, 0)

    def dfs(self, node: Optional[TreeNode], currSum: int) -> int:
        if not node:
            return 0

        currSum = currSum * 10 + node.val

        if not node.left and not node.right:
            return currSum

        return self.dfs(node.left, currSum) + self.dfs(node.right, currSum)