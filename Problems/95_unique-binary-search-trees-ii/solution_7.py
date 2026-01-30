# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        if n == 0: return []

        dp = [[] for _ in range(n+1)]
        dp[0] = [None]

        for length in range(1, n+1):
            for j in range(1, length+1):
                for leftTree in dp[j-1]:
                    for rightTree in dp[length-j]:
                        root = TreeNode(j)
                        root.left = leftTree
                        root.right = self.clone(rightTree, j)
                        dp[length].append(root)
        return dp[n]

    def clone(self, node: Optional[TreeNode], offset: int) -> Optional[TreeNode]:
        if node is None:
            return None

        newNode = TreeNode(node.val + offset)
        newNode.left = self.clone(node.left, offset)
        newNode.right = self.clone(node.right, offset)
        
        return newNode