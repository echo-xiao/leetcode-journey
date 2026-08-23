class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for c in s:
            if c.isalnum():
                clean = clean + c.lower()
        
        left = 0
        right = len(clean)-1
        while left < right:
            if clean[left] == clean[right]:
                left += 1
                right -= 1
            else:
                return False
        return True