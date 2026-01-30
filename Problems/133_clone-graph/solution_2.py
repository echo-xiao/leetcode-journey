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

        visited = {}

        return self.dfs(node, visited)

    def dfs(self, curr, visited):
        if curr in visited:
            return visited[curr]
        
        cloneNode = Node(curr.val)
        visited[curr] = cloneNode

        for neighbor in curr.neighbors:
            cloneNeighbor = self.dfs(neighbor, visited)
            cloneNode.neighbors.append(cloneNeighbor)

        return cloneNode