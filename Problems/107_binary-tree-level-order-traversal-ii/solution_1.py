# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = collections.deque([root])
        ans = []

        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(vals)
        return ans[::-1]