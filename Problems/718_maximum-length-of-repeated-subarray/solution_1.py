class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        n, m = len(nums1), len(nums2)
        ret = 0

        for i in range(n):
            length = min(m, n-i)
            currLen = self.getMaxLen(nums1, nums2, i, 0, length)
            ret = max(ret, currLen)
        
        for i in range(m):
            length = min(n, m-i)
            currLen = self.getMaxLen(nums1, nums2, 0, i, length)
            ret = max(ret, currLen)

        return ret



    def getMaxLen(self, nums1: List[int], nums2: List[int], addA: int, addB: int, length: int) -> int:
        cnt = 0
        maxVal = 0
    
        for i in range(length):
            if nums1[addA + i] == nums2[addB + i]:
                cnt += 1
                maxVal = max(maxVal, cnt)
            else:
                cnt = 0
        return maxVal
        