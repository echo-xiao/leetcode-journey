# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []
        self.dfs(root, targetSum, [], res)
        return res


    def dfs(self, node, sumVal, path, res):
        if not node:
            return []

        path.append(node.val)

        sumVal = sumVal - node.val
        if node.left is None and node.right is None:
            if sumVal == 0:
                res.append(list(path))

        leftTree = self.dfs(node.left, sumVal, path, res)
        rightTree = self.dfs(node.right, sumVal, path, res)

        path.pop()

        