# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = []
        curr = root
        stack = []

        while curr is not None or len(stack) > 0:
            while curr is not None:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.right
            node = stack.pop()
            curr = node.left
        return res[::-1]
