from collections import Counter

class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        n = len(nums)
        res_arr = []

        for l in range(0, n-k+1):
            win = nums[l: l+k]
            counts = Counter(win)
            res = 0
            
            if len(counts) < x:
                res = sum(win)
            else:
                freq = list(counts.items())
                freq.sort(key=lambda item: (item[1], item[0]), reverse=True)
            
                top = freq[0:x]

                for n, f in top:
                    res += n * f

            res_arr.append(res)

        return res_arr
            