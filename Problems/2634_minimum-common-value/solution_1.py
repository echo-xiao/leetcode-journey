class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        min_res = float('inf')
        for i in range(0, len(nums2)):
            target = nums2[i]
            left, right = 0, len(nums1)-1
            res = float('inf')
            while left <= right:
                mid = left + (right - left) // 2
                if nums1[mid] == target:
                    res = nums1[mid]
                    break
                elif nums1[mid] > target:
                    right = mid-1
                elif nums1[mid] < target:
                    left = mid+1
            min_res = min(res, min_res)
        if min_res == float('inf'):
            return -1
        else:
            return min_res
        