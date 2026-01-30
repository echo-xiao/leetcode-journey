# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root is None:
            return

        q = deque()
        q.append(root)
        depth = 1
        res = []

        while q:
            sz = len(q)
            ttl = 0

            for i in range(sz):
                cur = q.popleft()
                ttl += cur.val

                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)

            res.append(ttl / sz)
            
            depth += 1
        return res
