"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        self.traverse(root, res)

        return res

    def traverse(self, node: 'Node', res) -> int:
        if not node:
            return 

        for child in node.children:
            self.traverse(child, res)
        
        res.append(node.val)