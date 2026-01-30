# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        self.res = None
        self.dfs(original, cloned, target)
        return self.res

    def dfs(self, p: Optional[TreeNode], q: Optional[TreeNode], target: TreeNode) -> None:
        if not q or not q:
            return 

        if p is target:
            self.res = q
            return

        self.dfs(p.left, q.left, target)
        self.dfs(p.right, q.right, target)
