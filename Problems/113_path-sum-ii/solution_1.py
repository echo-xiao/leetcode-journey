# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        path = []

        self.dfs(root, targetSum, path, res)
        return res


    def dfs(self, node, targetSum, path, res):
        if not node:
            return []
    
        path.append(node.val)
        
        if not node.left and not node.right and targetSum == node.val:
            res.append(path[:])

        self.dfs(node.left, targetSum - node.val, path, res)
        self.dfs(node.right, targetSum - node.val, path, res)

        path.pop()

        
        