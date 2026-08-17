class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        cnt = 0
        for i in s[0:k]:
            if i in vowels:
                cnt += 1
        maxlen = cnt

        for left in range(1, len(s)-k+1):
            if s[left+k-1] in vowels:
                cnt += 1
            if s[left-1] in vowels:
                cnt -= 1
            maxlen = max(maxlen, cnt)
        return maxlen

