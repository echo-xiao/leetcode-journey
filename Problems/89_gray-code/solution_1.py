class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        res = [0]
        visited = {0}
        cnt = 1<<n # 计算总共有多少个数字。1 << n 等于 2^n。

        self.dfs(0, n, cnt, visited, res)
        return res


    def dfs(self, curr, n, cnt, visited, res):

        if len(res) == cnt:
            return True

        for i in range(n):
            # 核心位运算。通过将 curr 与 1 << i 进行异或 
            # 可以精准地只改变 curr 的第 i 位（从 0 变 1 或从 1 变 0）。
            # 这保证了 nxt 和 curr 之间汉明距离恰好为 1。

            nxt = curr ^ (1 << i) 

            if nxt not in visited:
                visited.add(nxt)
                res.append(nxt)

                if self.dfs(nxt, n, cnt, visited, res):
                    return True

                res.pop()
                visited.remove(nxt)

        return False