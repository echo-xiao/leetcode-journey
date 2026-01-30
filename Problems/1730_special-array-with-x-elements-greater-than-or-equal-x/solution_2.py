class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        
        left, right = 0, len(nums)
        while left <= right:
            guess = left + (right - left) // 2
            cnt = 0
            for num in nums:
                if num >= guess:
                    cnt += 1
            
            if cnt == guess:
                return guess
            elif cnt > guess:
                left = guess+1
            elif cnt < guess:
                right = guess-1

        return -1