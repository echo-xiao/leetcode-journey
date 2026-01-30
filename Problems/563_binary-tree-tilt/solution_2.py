# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.diff = 0
        
        self.sumTree(root)
        return self.diff

        

    def sumTree(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0


        leftSum = self.sumTree(node.left)
        rightSum = self.sumTree(node.right)

        self.diff += abs(leftSum - rightSum)
        

        return node.val + leftSum + rightSum