# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1

        # self.min1 就是全局最小值
        self.min1 = root.val
        # self.second_min 用来记录我们找到的大于 min1 的最小值
        self.second_min = float('inf')

        self.dfs(root)

        # 如果 self.second_min 从未被更新过，说明没有找到第二小值
        return self.second_min if self.second_min != float('inf') else -1

    def dfs(self, node: Optional[TreeNode]):
        # 终止条件
        if not node:
            return

        # 核心逻辑：
        # 如果当前节点的值已经大于 min1，它就是一个候选值。
        if node.val > self.min1:
            # 更新第二小值
            self.second_min = min(self.second_min, node.val)
            # 剪枝！因为它的子节点只会更大，所以无需继续向下探索此分支。
            return

        # 如果当前节点的值等于 min1 (根据题意，它不可能小于)，
        # 则第二小值可能存在于其子树中，必须继续向下。
        self.dfs(node.left)
        self.dfs(node.right)

