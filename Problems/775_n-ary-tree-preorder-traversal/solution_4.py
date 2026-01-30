"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        if root is None:
            return []

        stack = [root]
        res = []

        while len(stack) > 0:
            curr = stack.pop()
            res.append(curr.val)
            for child in reversed(curr.children):
                stack.append(child)
            
        return res

        # while curr is not None or len(stack) > 0:
        #     while curr is not None:
        #         res.append(curr.val)
        #         stack.append(curr)
        #         curr = curr.left


        #     if len(stack) > 0:
        #         node = stack.pop()
        #         curr = node.right

        # return res

            