class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, 0
        ttl, maxttl = 0, 0
        counter = defaultdict(int)

        for right in range(0, n):
            counter[nums[right]] += 1
            ttl += nums[right]
            
            while counter[nums[right]] > 1:
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]
                ttl -= nums[left]
                left += 1
            maxttl = max(ttl, maxttl)
        return maxttl
                