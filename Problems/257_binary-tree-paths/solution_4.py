# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        if not root:
            return res
        self.traverse(root, "", res)
        return res
    

    def traverse(self, node: Optional[TreeNode], path: str, res: List[str]):

        new_path = path + str(node.val)
        
        if node.left is None and node.right is None:
            res.append(new_path)
            return 
        
        if node.left:
            self.traverse(node.left, new_path + "->", res)
        if node.right:
            self.traverse(node.right, new_path + "->", res)


