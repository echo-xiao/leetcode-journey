class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = [nums[0]]
        
        for n in nums:
            if n > tail[-1]:
                tail.append(n)
            else:
                idx = self.search(tail, n)
                tail[idx] = n
        return len(tail)

    def search(self, tail: List[int], n: int) -> int:
        left, right = 0, len(tail)-1
        while left <= right:
            mid = left + (right - left) // 2
            if tail[mid] >= n:
                right = mid-1
            else:
                left = mid+1
        return left

            