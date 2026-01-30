class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        res = [0]
        visited = {0}
        cnt = 1 << n

        self.dfs(0, n, cnt, visited, res)
        return res




    def dfs(self, curr, n, cnt, visited, res):

        if len(res) == cnt:
            return True

        for i in range(n):
            nxt = curr ^ (1 << i)

            if nxt not in visited:
                visited.add(nxt)
                res.append(nxt)

                if self.dfs(nxt, n, cnt, visited, res):
                    return True

                res.pop()
                visited.remove(nxt)

        return False