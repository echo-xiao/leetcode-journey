# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []


        q = deque([root, None])
        res = []
        curr = root

        while q:
            prev, curr = curr, q.popleft()

            while curr is not None:
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
                prev, curr = curr, q.popleft()

            res.append(prev.val)

            if q:
                q.append(None)
        return res