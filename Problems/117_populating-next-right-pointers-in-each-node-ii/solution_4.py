"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        p = root.next
        nxt = None

        while p:
            if p.left:
                nxt = p.left
                break
            if p.right:
                nxt = p.right
                break
            p = p.next
        
        if root.right:
            root.right.next = nxt
        if root.left:
            root.left.next = root.right if root.right else nxt
        
        self.connect(root.right)
        self.connect(root.left)

        return root