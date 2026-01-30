class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = set()


        for target in nums2:
            if self.helper(nums1, target, 0, len(nums1)-1):
                res.add(target)
        return list(res)
            

    def helper(self, nums1: List[int], target: int, left: int, right: int) -> List[int]:

        if left > right:
            return False

        mid = left + (right - left) // 2

        if nums1[mid] == target:
            return True
        elif nums1[mid] > target:
            return self.helper(nums1, target, left, mid-1)
        elif nums1[mid] < target:
            return self.helper(nums1, target, mid+1, right)

            