class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums1)
        mapp = {}
        for i, num in enumerate(nums1):
            mapp[num] = i
        
        for i in range(len(nums2)-1, -1, -1):

            while len(stack) > 0 and stack[-1] <= nums2[i]:
                stack.pop()

            if nums2[i] in mapp:
                if len(stack) > 0 and stack[-1] > nums2[i]:
                    idx = mapp[nums2[i]]
                    res[idx] = stack[-1]
            
            stack.append(nums2[i])
        return res