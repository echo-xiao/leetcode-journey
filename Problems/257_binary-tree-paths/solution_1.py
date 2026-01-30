# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []

        res = []
        self.traverse(root, "", res)
        return res


    def traverse(self, node: Optional[TreeNode], path: str, res: List[int]):
        if not node:
            return 

        new_path = path + str(node.val)

        if not node.left and not node.right:
            res.append(new_path)
            return res

        self.traverse(node.left, new_path + "->", res)
        self.traverse(node.right, new_path + "->", res)