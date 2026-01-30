
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

       self.res = 0
       self.traverse(root, 0)
       return self.res


    def traverse(self, node: Optional[TreeNode], ttl: int):
        if not node:
            return
        
        ttl = (ttl * 2) + node.val

        if not node.left and not node.right:
            self.res += ttl

        self.traverse(node.left, ttl)
        self.traverse(node.right, ttl)



