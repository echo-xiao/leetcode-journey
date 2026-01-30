class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        

        stack = []
        mapp = {}
        res = [-1] * len(nums1)

        for i in range(0, len(nums2)):
            num = nums2[i]
            while len(stack) > 0 and num > stack[-1]:
                tmp = stack.pop()
                mapp[tmp] = num
            stack.append(num)
                
        for n in range(0, len(nums1)):
            if nums1[n] in mapp:
                res[n] = mapp[nums1[n]]
            else:
                res[n] = -1
        return res