# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        self.res = []
        self.path = []
        self.dfs(root, targetSum)
        return self.res

    
    def dfs(self, node: Optional[TreeNode], targetSum: int):
        if not node:
            return 

        currSum = targetSum - node.val
        self.path.append(node.val)

        if not node.left and not node.right and currSum == 0:
            self.res.append(list(self.path))

        self.dfs(node.left, currSum)
        self.dfs(node.right, currSum)

        self.path.pop()