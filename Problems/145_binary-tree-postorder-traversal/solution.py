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
        prev = None

        while curr is not None or len(stack) > 0:
            while curr is not None:
                stack.append(curr)
                curr = curr.left


            peek = stack[-1]
            if peek.right is not None and prev != peek.right:
                node = stack[-1]
                curr = node.right
            elif prev == peek.right or peek.right is None:
                node = stack.pop()
                res.append(node.val)
                prev = node

            
        return res
