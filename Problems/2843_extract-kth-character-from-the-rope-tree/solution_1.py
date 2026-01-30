# Definition for a rope tree node.
# class RopeTreeNode(object):
#     def __init__(self, len=0, val="", left=None, right=None):
#         self.len = len
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        if not root:
            return 
        self.res = ""
        self.dfs(root)
        return self.res[k-1]
        

    def dfs(self, node: Optional[object]) -> str:
        if not node:
            return

        self.dfs(node.left)

        if node.left is None and node.right is None:
            self.res = self.res + node.val

        self.dfs(node.right)