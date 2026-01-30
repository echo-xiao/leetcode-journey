# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        stack = []
        node = root
        prev = TreeNode(float('-inf'))
        first = second = None
        

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            

            if prev.val > node.val:
                if not first:
                    first = prev
                second = node
            prev = node

            
            node = node.right
            

        first.val, second.val = second.val, first.val