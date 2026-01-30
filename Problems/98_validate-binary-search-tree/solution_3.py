# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.tag = True
        self.prev = float('-inf')
        self.inorder(root)
        return self.tag

    def inorder(self, node):
        if not node or not self.tag:
            return

        self.inorder(node.left)

        if self.prev >= node.val:
            self.tag = False
            return 

        self.prev = node.val

        self.inorder(node.right)

        