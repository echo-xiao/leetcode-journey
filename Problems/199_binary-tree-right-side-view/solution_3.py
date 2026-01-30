# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []
            
        q = collections.deque([root])
        res = []

        while q:
            size = len(q)
            vals = []
            for i in range(size):
                node = q.popleft()
                vals.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            res.append(vals[-1])
        return res