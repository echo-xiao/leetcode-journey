# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return self.traverse(root)


    def traverse(self, node: Optional[TreeNode]) -> bool:
        if not node:
            return 

        if node.val == 1:
            return True
        elif node.val == 0:
            return False


        leftCheck = self.traverse(node.left)
        rightCheck = self.traverse(node.right)

        if node.val == 2:
            return leftCheck or rightCheck
        elif node.val == 3:
            return leftCheck and rightCheck


