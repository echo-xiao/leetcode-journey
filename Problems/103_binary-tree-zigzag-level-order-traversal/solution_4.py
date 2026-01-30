# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        
        self.traverse(root, 0, res)

        return [list(d) for d in res]

    def traverse(self, node: Optional[TreeNode], level: int, res: List[int]):
        if not node:
            return 

        if len(res) == level:
            res.append(deque())

        if level % 2 == 0:
            res[level].append(node.val)
        else:
            res[level].appendleft(node.val)

        self.traverse(node.left, level+1, res)
        self.traverse(node.right, level+1, res)
        