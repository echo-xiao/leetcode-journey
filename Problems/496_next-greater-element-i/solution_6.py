class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        mapp = {}
        ans = []

        for i in range(len(nums2)-1, -1, -1):
            
            while len(stack) > 0 and nums2[i] >= stack[-1]:
                stack.pop()
            
            if len(stack) == 0:
                mapp[nums2[i]] = -1
            else:
                top = stack[-1]
                mapp[nums2[i]] = top
            
            stack.append(nums2[i])

        for i in nums1:
            ans.append(mapp[i])
        return ans