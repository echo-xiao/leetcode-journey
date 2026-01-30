class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums1)
        
        for i in range(len(nums2)-1, -1, -1):
            
            while len(stack) > 0 and stack[-1] <= nums2[i]:
                stack.pop()

            if nums2[i] in nums1:
                idx = nums1.index(nums2[i])
                if len(stack) > 0:
                    res[idx] = stack[-1]
                else:
                    res[idx] = -1
            stack.append(nums2[i])

        return res