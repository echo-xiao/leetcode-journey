class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        maxLen = 0
        cnt = 0


        while right < len(nums):
            if nums[right] == 0:
                cnt += 1
            right += 1

            while cnt > k:
                if nums[left] == 0:
                    cnt -= 1
                left += 1

            maxLen = max(maxLen, right-left)
        
        return maxLen