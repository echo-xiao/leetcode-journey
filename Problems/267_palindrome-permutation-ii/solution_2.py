class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        count = Counter(s)

        mid = ""
        half = []
        oddCnt = 0

        for char, freq in count.items():
            if freq % 2 == 1:
                oddCnt += 1
                mid = char
            half.extend([char] * (freq//2))

        if oddCnt > 1:
            return []

        res = []
        half.sort()
        used = [False] * len(half)

        self.dfs(half, used, [], mid, res)
        return res

    def dfs(self, nums, used, path, mid, res):
        if len(path) == len(nums):
            left = "".join(path)
            res.append(left + mid + left[::-1])
            return 

        for i in range(len(nums)):
            if used[i]:
                continue

            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue

            used[i] = True
            path.append(nums[i])
            self.dfs(nums, used, path, mid, res)
            path.pop()
            used[i] = False
        