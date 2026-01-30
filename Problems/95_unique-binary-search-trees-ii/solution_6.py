# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        

        if n == 0:
            return []

        return self.generate(1, n)

    def generate(self, left, right):
        
        if left > right:
            return [None]

        trees = []

        for i in range(left, right+1):
            leftTrees = self.generate(left, i-1)
            rightTrees = self.generate(i+1, right)

            for l in leftTrees:
                for r in rightTrees:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    trees.append(root)

        return trees
