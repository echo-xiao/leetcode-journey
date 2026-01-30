class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        self.charToStr = {}
        self.usedStrs = set()

        return self.isMatch(pattern, 0, s, 0)

    def isMatch(self, pattern, pidx, s, sidx) -> bool:
        if pidx == len(pattern):
            return sidx == len(s)

        char = pattern[pidx]

        if char in self.charToStr:
            target = self.charToStr[char]
            if not s.startswith(target, sidx):
                return False
            return self.isMatch(pattern, pidx+1, s, sidx+len(target))

        for end in range(sidx+1, len(s)+1):
            sub = s[sidx: end]

            if sub in self.usedStrs:
                continue

            self.charToStr[char] = sub
            self.usedStrs.add(sub)

            if self.isMatch(pattern, pidx+1, s, end):
                return True

            del self.charToStr[char]
            self.usedStrs.remove(sub)

        return False