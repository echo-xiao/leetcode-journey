class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean = ""
        for c in s:
            if c.isalnum():
                clean += c.lower()
        
        left = 0
        right = len(clean)-1
        while left < right:
            if clean[left] != clean[right]:
                return False
            else:
                left += 1
                right -= 1
        return True