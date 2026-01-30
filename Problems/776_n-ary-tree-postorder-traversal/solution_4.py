"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.res = []

        self.traverse(root)

        return self.res

    def traverse(self, node: 'Node'):
        if not node:
            return []

        for child in node.children:
            self.traverse(child)
        
        self.res.append(node.val)