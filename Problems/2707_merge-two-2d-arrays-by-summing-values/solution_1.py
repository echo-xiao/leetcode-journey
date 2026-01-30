class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        i, j, k = 0, 0, 0
        nums = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i][0] == nums2[j][0]:
                left = nums1[i][0]
                right = nums1[i][1] + nums2[j][1]
                nums.append([left, right])
                i += 1
                j += 1
            elif nums1[i][0] > nums2[j][0]:
                left = nums2[j][0]
                right = nums2[j][1]
                nums.append([left, right])
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                left = nums1[i][0]
                right = nums1[i][1]
                nums.append([left, right])
                i += 1

        while i >= len(nums1) and j < len(nums2):
            left = nums2[j][0]
            right = nums2[j][1]
            nums.append([left, right])
            j += 1

        while i < len(nums1) and j <= len(nums2):
            left = nums1[i][0]
            right = nums1[i][1]
            nums.append([left, right])
            i += 1
        return nums