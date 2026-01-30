class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = len(nums1) * [-1]
        for i in range(0, len(nums1)):
            idx = nums2.index(nums1[i])
            for j in range(idx+1, len(nums2)):
                if nums2[j] > nums1[i]:
                    res[i] = nums2[j]
                    break
        return res