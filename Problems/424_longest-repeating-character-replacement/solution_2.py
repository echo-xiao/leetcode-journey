class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        left, right = 0, 0
        maxlen = 0
        n = len(s)
        for right in range(0, len(s)):
            counter[s[right]] += 1
            winlen = right-left+1
            mostfreq = max(counter.values())
            while (right-left+1) - max(counter.values()) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            maxlen = max(maxlen, right-left+1)
        return maxlen