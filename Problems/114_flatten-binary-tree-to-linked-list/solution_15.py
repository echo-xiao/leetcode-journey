class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return 
        res = []
        stack = []
        curr = root
        
        while curr is not None or stack:
            if curr is not None:
                res.append(curr)
                stack.append(curr)
                curr = curr.left
            else:
                node = stack.pop()
                curr = node.right


        for i in range(0, len(res)-1):
            res[i].left = None
            res[i].right = res[i+1]
        
        res[-1].left = None
        res[-1].right = None