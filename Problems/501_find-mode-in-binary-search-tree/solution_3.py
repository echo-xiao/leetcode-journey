# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.curr = None
        self.cnt = 0
        self.max_res = 0

        self.traverse(root)
        return self.res



    def traverse(self, node: Optional[TreeNode]) -> int:

        if not node:
            return

        self.traverse(node.left)

        if self.curr == node.val:
            self.cnt += 1
        else:
            self.curr = node.val
            self.cnt = 1
        
        if self.cnt > self.max_res:
            self.max_res = self.cnt
            self.res = [self.curr]
        elif self.cnt == self.max_res:
            self.res.append(self.curr)
        
        self.traverse(node.right)
        
