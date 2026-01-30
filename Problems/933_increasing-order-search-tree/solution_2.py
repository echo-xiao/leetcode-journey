# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        self.dummy_head = TreeNode(-1)
        self.node = self.dummy_head

        self.traverse(root)

        return self.dummy_head.right


    def traverse(self, node: Optional[TreeNode]):

        if not node:
            return 

        self.traverse(node.left)
        self.node.right = TreeNode(node.val)
        self.node = self.node.right
        self.traverse(node.right)

        return self.dummy_head.right