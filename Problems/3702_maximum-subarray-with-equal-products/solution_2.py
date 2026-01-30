import math

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = 1

        for left in range(0, n):
            g = l = p = nums[left]

            for right in range(left + 1, n):
                x = nums[right]
                p = p * x
                l = math.lcm(l, x)
                g = math.gcd(g, x)

                if p == l * g:
                    res = max(res, right - left + 1)
        return res