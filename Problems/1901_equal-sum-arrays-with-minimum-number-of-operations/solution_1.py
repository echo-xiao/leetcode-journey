class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:

        s1, s2 = sum(nums1), sum(nums2)
        if s2 > s1:
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1
        diff = s1 - s2
        if diff == 0:
            return 0

        gains = []
        for i in nums1:
            gains.append(i-1)
        for j in nums2:
            gains.append(6-j)
        gains.sort(reverse=True)

        ops = 0
        for g in gains:
            diff -= g
            ops += 1
            if diff <= 0:
                return ops
        return -1