# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []

        self.dfs(root, None)
        return self.res

    def dfs(self, node: Optional[TreeNode], prev: Optional[TreeNode]):
        if not node:
            return

        if prev is not None and ((prev.left is None and prev.right is not None) or (prev.left is not None and prev.right is None)):
            self.res.append(node.val)

        self.dfs(node.left, node)
        self.dfs(node.right, node)