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
        self.traverse(root, 0)
        return [s/c for s, c in self.stats]
        

    def traverse(self, node: Optional[TreeNode], level: int):
        if not node:
            return

        if level == len(self.stats):
            self.stats.append([0, 0])

        self.stats[level][0] += node.val
        self.stats[level][1] += 1

        self.traverse(node.left, level+1)
        self.traverse(node.right, level+1)