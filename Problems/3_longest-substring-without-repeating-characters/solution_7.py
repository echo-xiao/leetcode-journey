class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = defaultdict(int)
        left = 0 
        right = 0
        maxlen = 0

        for right in range(0, len(s)):
            
            while s[right] in counter:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            counter[s[right]] += 1
            maxlen = max(maxlen, right-left+1)
    
        return maxlen