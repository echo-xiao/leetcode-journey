# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        self.index = 0
        self.nums = nums
        return self.build(0, len(nums)-1)

        
    def build(self, left, right):
        if left > right:
            return None

        mid = (left + right) // 2

        leftTree = self.build(left, mid-1)
        root = TreeNode(self.nums[self.index])
        self.index += 1
        root.left = leftTree
        root.right = self.build(mid+1, right)

        return root


    # 强行模拟中序遍历

    

