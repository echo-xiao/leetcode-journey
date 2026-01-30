# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        leftInvert = self.invertTree(root.left)
        rightInvert = self.invertTree(root.right)

        root.left = rightInvert
        root.right = leftInvert

        return root


        # 后序遍历