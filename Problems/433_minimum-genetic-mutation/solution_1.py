class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        queue = collections.deque([(startGene, 0)])
        visited = {startGene}
        while queue:
            curr, step = queue.popleft()

            if curr == endGene:
                return step

            for i in range(len(curr)):
                for char in 'ACGT':
                    nxt_gene = curr[:i] + char + curr[i+1:]
                    if nxt_gene in bank_set and nxt_gene not in visited:
                        visited.add(nxt_gene)
                        queue.append((nxt_gene, step+1))
        return -1