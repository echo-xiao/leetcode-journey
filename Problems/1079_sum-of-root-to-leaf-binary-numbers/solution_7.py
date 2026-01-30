# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ttl_sum = 0
        # if not root:
        #     return 0

        # return self.dfs(root, 0)
        self.dfs(root, 0)
        return self.ttl_sum


    def dfs(self, node: Optional[TreeNode], ttl: int) -> int:
        if not node:
            return 

        ttl = (ttl * 2) + node.val

        if node.left is None and node.right is None:
            self.ttl_sum += ttl
            return 
        
        self.dfs(node.left, ttl)
        self.dfs(node.right, ttl)

        # if node.left is None and node.right is None:
        #     return ttl
            
        # leftSum = self.dfs(node.left, ttl)
        # rightSum = self.dfs(node.right, ttl)

        # return leftSum + rightSum