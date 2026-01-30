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

        memo = {}

        return self.buildTrees(1, n, memo)

    def buildTrees(self, left: int, right: int, memo: dict) -> Optional[TreeNode]:

        if left > right:
            return [None]

        if (left, right) in memo:
            return memo[(left, right)]

        res = []

        for i in range(left, right+1):
            leftTree = self.buildTrees(left, i-1, memo)
            rightTree = self.buildTrees(i+1, right, memo)

            for l in leftTree:
                for r in rightTree:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    res.append(node)
        
        memo[(left, right)] = res
        return res

