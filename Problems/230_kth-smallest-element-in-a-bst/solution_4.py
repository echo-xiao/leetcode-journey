# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.k = k
        self.res = None
        self.dfs(root)
        return self.res

    def dfs(self, node) -> int:
        if not node:
            return None

        self.dfs(node.left)

        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return self.res

        self.dfs(node.right)
    


