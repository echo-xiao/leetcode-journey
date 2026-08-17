class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:

        s1 = sum(nums1)
        s2 = sum(nums2)

        if s1 - s2 > 0:
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1
        diff = s2 - s1
        if diff == 0:
            return 0

        gains = []
        for i in nums1:
            gains.append(6-i)
        for j in nums2:
            gains.append(j-1)
        gains.sort(reverse=True)

        ops = 0
        for k in gains:
            diff -= k
            ops += 1
            if diff <= 0:
                return ops
        return -1
        
        