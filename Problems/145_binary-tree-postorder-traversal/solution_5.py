# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root
        prev = None

        while curr is not None or len(stack) > 0:    

            while curr is not None:
                stack.append(curr)
                curr = curr.left
        
            if len(stack) > 0:
                peek = stack[-1]

                if peek.right is None or peek.right == prev:
                    node = stack.pop()
                    res.append(node.val)
                    prev = node
                    curr = None
                else:
                    curr = peek.right

        return res

