class Solution:
    def maxScore(self, s: str) -> int:
        arr0 = [0] * (len(s)+1)
        arr1 = [0] * (len(s)+1)


        for i in range(0, len(s)):
            if s[i] == '0':
                arr0[i+1] = arr0[i] + 1
                arr1[i+1] = arr1[i]
            elif s[i] == '1':
                arr0[i+1] = arr0[i]
                arr1[i+1] = arr1[i] + 1

            
        res = []
        for i in range(1, len(s)):
            left = arr0[i]
            right = arr1[-1] - arr1[i]
            ttl = left + right
            res.append(ttl)

        return max(res)
        