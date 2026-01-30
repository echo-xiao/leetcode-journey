class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []
        self.dfs(s, 0, path, res)        
        return res

    def dfs(self, s, start, path, res):
        if start == len(s):
            res.append(path[:])
            return

        for i in range(start, len(s)):
            seg = s[start: i+1]
            if seg == seg[::-1]:
                path.append(seg)
                self.dfs(s, i+1, path, res)
                path.pop()