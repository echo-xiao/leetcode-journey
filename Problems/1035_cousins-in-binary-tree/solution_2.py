# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False

        self.dx = -1
        self.dy = -1
        self.px = None
        self.py = None
        self.x = x
        self.y = y


        return self.traverse(root, None, 0)

    def traverse(self, node: Optional[TreeNode], prev: Optional[int], depth: int) -> bool:
        if not node:
            return 

        if node.val == self.x:
            self.px = prev
            self.dx = depth

        if node.val == self.y:
            self.py = prev
            self.dy = depth

        self.traverse(node.left, node, depth+1)
        self.traverse(node.right, node, depth + 1)

        return self.dx == self.dy and self.px != self.py