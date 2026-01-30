class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        index =  self.helper(letters, target, 0, len(letters)-1)
        return letters[index % len(letters)]
        
    def helper(self, letters: List[str], target: int, left: int, right: int) -> int:
        if left > right:
            return left
        
        mid = left + (right - left) // 2
        
        if letters[mid] > target:
            return self.helper(letters, target, left, mid-1)
        elif letters[mid] <= target:
            return self.helper(letters, target, mid+1, right)
