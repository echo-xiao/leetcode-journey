class Solution(object):
    def minimumSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        l = 0 
        win_or = 0
        min_length = float('inf')
        bit_counts = [0] * 32

        for r in range(0, len(nums)):
            for i in range(32):
                if (nums[r] >> i) & 1:
                    bit_counts[i] += 1

            win_or = 0
            for i in range(32):
                if bit_counts[i] > 0:
                    win_or |= (1 << i)

            while win_or >= k and l <= r:
                length = r - l + 1
                min_length = min(length, min_length)

                for i in range(32):
                    if (nums[l] >> i) & 1:
                        bit_counts[i] -= 1

                win_or = 0
                for i in range(32):
                    if bit_counts[i] > 0:
                        win_or |= (1 << i)

                
                l += 1
        
        if min_length == float('inf'):
            return -1
        else:
            return min_length