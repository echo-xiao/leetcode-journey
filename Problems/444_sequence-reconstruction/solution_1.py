class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        indegree = [0] * (n+1)
        adj = [[] for _ in range(n+1)]
        
        for seq in sequences:
            for i in range(len(seq)-1):
                u, v = seq[i], seq[i+1]
                adj[u].append(v)
                indegree[v] += 1

        queue = collections.deque([i for i in range(1, n+1) if indegree[i] == 0])

        res = []
        while queue:
            if len(queue) > 1:
                return False

            curr = queue.popleft()
            res.append(curr)

            for neighbor in adj[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return res == nums