# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        curr = root
        dummy = TreeNode(-1)
        stack = []
        prev = dummy
        
        while curr is not None or len(stack) > 0:

            while curr is not None:
                stack.append(curr)
                curr = curr.left
            
            node = stack.pop()
            
            node.left = None
            prev.right = node
            prev = node

            curr = node.right
        return dummy.right
            
