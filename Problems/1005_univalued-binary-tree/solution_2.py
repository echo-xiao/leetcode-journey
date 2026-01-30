# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # 1. 如果是空树，直接返回 True
        if not root:
            return True
        
        # 2. 对于非空树，获取目标值，并开始遍历检查
        targetVal = root.val
        return self.traverse(root, targetVal)

    # 你的 traverse 函数是正确的，无需修改
    def traverse(self, node: Optional[TreeNode], targetVal: int) -> bool:
        if not node:
            return True

        if node.val != targetVal:
            return False

        leftCheck = self.traverse(node.left, targetVal)
        rightCheck = self.traverse(node.right, targetVal)

        return leftCheck and rightCheck