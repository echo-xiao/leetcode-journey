class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        left, right = 0, len(letters)-1
        while left < right:
            mid = left + (right - left) // 2
            if letters[mid] > target:
                right = mid
            elif letters[mid] <= target:
                left = mid + 1
        
        if letters[left] > target:
            return letters[left]
        else:
            return letters[0]
            