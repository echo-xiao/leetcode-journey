# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return targetSum == None

        return self.traverse(root, 0, targetSum)


    def traverse(self, node: Optional[TreeNode], res: int, targetSum: int) -> bool:

        if not node:
            return False
            
        new_res = res + node.val

        if node.left is None and node.right is None:
            return new_res == targetSum

        leftCheck = self.traverse(node.left, new_res, targetSum)
        rightCheck = self.traverse(node.right, new_res, targetSum)

        return leftCheck or rightCheck