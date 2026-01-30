# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        return self.dfs(root, 0)

    def dfs(self, node, num) -> List[int]:

        if node is None:
            return 0

        num = num * 10 + node.val
        
        if not node.left and not node.right:
            return num

        leftSum = self.dfs(node.left, num)
        rightSum = self.dfs(node.right, num)

        return leftSum + rightSum