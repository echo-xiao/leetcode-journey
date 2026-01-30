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

        while curr is not None or stack: #算法何时停止运行，len(stack) > 0 或者 curr还没有到最底部

            

            while curr is not None:
                res.append(curr.val)
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            curr = curr.right

        return res

    
        