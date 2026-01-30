# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []

        self.dfs(root)
        return self.res

    def dfs(self, node: Optional[TreeNode]):
        if not node:
            return

        if node.left is None and node.right is not None:
            self.res.append(node.right.val)
            
        if node.left is not None and node.right is None:
            self.res.append(node.left.val)

        self.dfs(node.left)
        self.dfs(node.right)