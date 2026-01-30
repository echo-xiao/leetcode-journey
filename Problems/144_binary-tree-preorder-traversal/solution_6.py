# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        curr = root
        


        while curr is not None or len(stack) > 0:
            while curr is not None:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.left

            if len(stack) > 0:
                node = stack.pop()
                curr = node.right

        return res

            

    
        