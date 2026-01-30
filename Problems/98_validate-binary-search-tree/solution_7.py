# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.prev = None
        return self.traverse(root)

    def traverse(self, node: Optional[TreeNode]) -> bool:

        if not node:
            return True

        if not self.traverse(node.left):
            return False

        if self.prev and self.prev.val >= node.val:
            return False

        self.prev = node

        return self.traverse(node.right)

    