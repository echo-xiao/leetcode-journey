class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        cnt = 0
        left = 0
        right = 0
        counter = defaultdict(int)

        for right in range(0, n):
            while s[right] in counter:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            counter[s[right]] += 1
            cnt = max(cnt, right-left+1)
        return cnt
                