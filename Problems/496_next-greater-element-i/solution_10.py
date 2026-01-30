class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        mapp = {}
        stack = []
        res = []

        for i in range(len(nums2)-1, -1, -1):
            num = nums2[i]
            while len(stack) > 0 and num >= stack[-1]:
                stack.pop()

            if len(stack) == 0:
                mapp[num] = -1
            else:
                mapp[num] = stack[-1]
            
            stack.append(num)

        for i in nums1:
            res.append(mapp[i])
        
        return res