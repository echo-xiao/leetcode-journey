"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        curr = head
        oldNode = {}

        while curr:
            oldNode[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            newNode = oldNode[curr]

            if curr.next:
                newNode.next = oldNode[curr.next]

            if curr.random:
                newNode.random = oldNode[curr.random]
            
            curr = curr.next

        return oldNode[head]