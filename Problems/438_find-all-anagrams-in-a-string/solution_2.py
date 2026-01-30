class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if s is None:
            return []
        
        freq = {}
        dic = {}
        for char in p:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

        length = len(p)

        res = []
        left, right = 0, 0
        valid = 0

        while right < len(s):
            c = s[right]
            right += 1

            if c in freq:
                if c not in dic:
                    dic[c] = 1
                else:
                    dic[c] += 1

                if dic[c] == freq[c]:
                    valid += 1
            while right - left >= len(p):
                if valid == len(freq):
                    res.append(left)
                d = s[left]
                left += 1

                if d in freq:
                    if freq[d] == dic[d]:
                        valid -= 1
                    dic[d] -= 1
        return res
