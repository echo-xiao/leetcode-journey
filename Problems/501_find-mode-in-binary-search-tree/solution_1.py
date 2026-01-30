# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        self.prev = None
        self.cnt = 0
        self.max_cnt = 0
        self.res = []

        if not root:
            return []

        self.traverse(root)
        return self.res


    def traverse(self, node: Optional[TreeNode]):

        if not node:
            return

        self.traverse(node.left)

        if self.prev == node.val:
            self.cnt += 1
        else:
            self.cnt = 1
        
        self.prev = node.val

        if self.cnt > self.max_cnt:
            self.max_cnt = self.cnt
            self.res = [self.prev]
        elif self.cnt == self.max_cnt:
            self.res.append(self.prev)

        self.traverse(node.right)

