"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
            
        queue = collections.deque()        
        cloneNode = Node(node.val)
        queue.append(node)
        
        visited = {}
        visited[node] = cloneNode

        while queue:
            curr = queue.popleft()

            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                visited[curr].neighbors.append(visited[neighbor])
        return visited[node]
