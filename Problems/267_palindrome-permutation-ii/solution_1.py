
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counts = collections.Counter(s)
        mid = ""
        half = []
        oddCnt = 0

        for char, count in counts.items():
            if count % 2 == 1:
                oddCnt += 1
                mid = char
                if oddCnt > 1:
                    return []

            half.extend([char]*(count//2))

        half.sort()
        path = []
        res = []
        used = [False] * len(half)
        self.dfs(half, used, path, res, mid)
        return res

    def dfs(self, half, used, path, res, mid):
        if len(path) == len(half):
            left = "".join(path)
            res.append(left + mid + left[::-1])
            return

        for i in range(len(half)):

            if used[i]:
                continue 

            if i > 0 and half[i] == half[i-1] and not used[i-1]:
                continue

            used[i] = True
            path.append(half[i])
            self.dfs(half, used, path, res, mid)
            path.pop()
            used[i] = False