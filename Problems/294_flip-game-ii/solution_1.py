class Solution:
    def canWin(self, currentState: str) -> bool:

        memo = {}

        def solve(s):
            if s in memo:
                return memo[s]

            for i in range(len(s)-1):
                seg = s[i: i+2]

                if seg == '++':
                    nxt = s[:i] + '--' + s[i+2:]

                    if not self.canWin(nxt):
                        return True
            memo[s] = False
            return False

        return solve(currentState)