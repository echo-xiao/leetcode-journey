# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
       
        if not root:
            return []

        self.stats = []
        res = []

        self.traverse(root, 0)
        for x, y in self.stats:
            res.append(x / y)
        return res

    def traverse(self, node: Optional[TreeNode], depth: int):
        if not node:
            return 

        if depth == len(self.stats):
            self.stats.append([0, 0])

        self.stats[depth][0] += node.val
        self.stats[depth][1] += 1
        
        new_depth = depth + 1
        self.traverse(node.left, new_depth)
        self.traverse(node.right, new_depth)
