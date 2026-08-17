class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counter = defaultdict(int)
        sumnum = 0
        maxnum = 0


        for i in range(0, k):
            sumnum += nums[i]
            counter[nums[i]] += 1
        
        if len(counter) == k:
            maxnum = sumnum


        for i in range(k, len(nums)):
            sumnum += nums[i]
            sumnum -= nums[i-k]

            counter[nums[i]] += 1
            counter[nums[i-k]] -= 1

            if counter[nums[i-k]] == 0:
                del counter[nums[i-k]]
            
            if len(counter) == k:
                maxnum = max(maxnum, sumnum)
        
        return maxnum

        