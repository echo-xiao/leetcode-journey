# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = None
        cnt = 0
        max_res = 0



        def traverse(node):

            if not node:
                return

            nonlocal res, max_res, curr, cnt

            traverse(node.left)

            if curr == node.val:
                cnt += 1
            else:
                curr = node.val
                cnt = 1
            
            if cnt > max_res:
                max_res = cnt
                res = [curr]
            elif cnt == max_res:
                res.append(curr)
            
            traverse(node.right)
        

        traverse(root)
        return res
