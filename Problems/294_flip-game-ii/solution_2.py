class Solution:
    def canWin(self, currentState: str) -> bool:

        for i in range(len(currentState)-1):
            seg = currentState[i: i+2]

            if seg == '++':
                nxt = currentState[:i] + '--' + currentState[i+2:]

                if not self.canWin(nxt):
                    return True

        return False