# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        self.res = 0
        self.traverse(root)
        return self.res


    def traverse(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        leftSum = self.traverse(node.left)
        rightSum = self.traverse(node.right)

        diff = abs(leftSum - rightSum)
        self.res += diff

        return leftSum + rightSum + node.val


        
        

