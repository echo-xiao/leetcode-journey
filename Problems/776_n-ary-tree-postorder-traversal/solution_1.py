"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        res = []
        stack = [root]


        while len(stack) > 0:
            curr = stack.pop()
            res.append(curr.val)
            for child in curr.children:
                stack.append(child)
        
        return reversed(res)