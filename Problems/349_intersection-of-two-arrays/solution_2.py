class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = set()

        for target in nums2:
            left, right = 0, len(nums1)-1
            while left <= right:
                mid = left + (right - left) // 2
                if nums1[mid] == target:
                    res.add(nums1[mid])
                    break
                elif nums1[mid] > target:
                    right = mid - 1
                elif nums1[mid] < target:
                    left = mid + 1
        return list(res)
                
            