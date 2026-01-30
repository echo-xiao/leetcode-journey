# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        stack = [(root, False)]
        prev = float('-inf')

        while stack:
            node, visited = stack.pop()
            
            if node is None:
                continue

            if visited:
                if node.val <= prev:
                    return False
                prev = node.val
                    
            else:

                if node.right:
                    stack.append((node.right, False))
                
                stack.append((node, True))
                
                if node.left:
                    stack.append((node.left, False))

        return True