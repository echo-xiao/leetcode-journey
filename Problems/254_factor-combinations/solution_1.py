class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        path = []
        self.dfs(n, 2, path, res)
        return res


    def dfs(self, target, start, path, res):

        for i in range(start, int(target**0.5)+1):
            if target % i == 0:
                res.append(path + [i, target // i])
                
                path.append(i)
                self.dfs(target // i, i, path, res)
                path.pop()

            

        # if target == 1:
        #     if len(path) > 1:
        #         res.append(path[:])
        #     return

        # for i in range(start, target+1):
        #     if target % i == 0:
        #         path.append(i)
        #         self.dfs(target // i, i, path, res)
        #         path.pop()
