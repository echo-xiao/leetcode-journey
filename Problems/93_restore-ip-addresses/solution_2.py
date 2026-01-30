class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []
        self.dfs(s, 0, [], res)
        return res


    def dfs(self, s, start, path, res):

        if len(path) == 4:
            if start == len(s):
                res.append(".".join(path))
            return 

        rem = 4 - len(path)
        if len(s) - start > rem * 3 or len(s) - start < rem:
            return 

        for size in range(1, 4):
            if start + size > len(s):
                break

            segment = s[start: start+size]

            if (size > 1 and segment[0] == '0') or int(segment) > 255:
                continue


            path.append(segment)
            self.dfs(s, start+size, path, res)
            path.pop()


