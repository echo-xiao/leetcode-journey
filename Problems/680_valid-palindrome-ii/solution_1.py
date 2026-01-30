class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                leftCheck = self.ifPalindrome(s, left+1, right)
                rightCheck = self.ifPalindrome(s, left, right-1)
                return leftCheck or rightCheck

            left += 1
            right -=1
        return True
        
            

    def ifPalindrome(self, s: str, left: int, right: int) -> bool:

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
                break
        return True
        
