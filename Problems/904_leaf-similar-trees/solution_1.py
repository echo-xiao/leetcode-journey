# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True

        res1 = []
        res2 = []
        
        res1 = self.traverse(root1, res1)
        res2 = self.traverse(root2, res2)

        return res1 == res2

    def traverse(self, node: Optional[TreeNode], res: List[int]):
        if not node:
            return

        self.traverse(node.left, res)
        self.traverse(node.right, res)

        if node.left is None and node.right is None:
            res.append(node.val)

        return res
        

        