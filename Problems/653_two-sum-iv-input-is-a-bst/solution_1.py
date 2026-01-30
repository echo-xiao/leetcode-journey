# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        res = set()

        return self.traverse(root, k, res)
        

    def traverse(self, node: Optional[TreeNode], k: int, res: set) -> bool:

        if not node:
            return False

        left = self.traverse(node.left, k, res)
        right = self.traverse(node.right, k, res)

        if (k - node.val) in res:
            return True
        else:
            res.add(node.val)
        
        return left or right