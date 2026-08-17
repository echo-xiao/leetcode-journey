class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        num = 0
        maxnum = 0

        for i in range(0, k):
            num += nums[i]
            counter[nums[i]] += 1
        if len(counter) == k:
            maxnum = num


        for j in range(k, len(nums)):
            num += nums[j]
            num -= nums[j-k]

            counter[nums[j]] += 1
            counter[nums[j-k]] -= 1

            if counter[nums[j-k]] == 0:
                del counter[nums[j-k]]

            if len(counter) == k:
                maxnum = max(maxnum, num)
        return maxnum
        