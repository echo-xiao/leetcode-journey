class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        counter = defaultdict(int)
        num = 0
        maxnum = 0
        
        for i in range(0, k):
            num += nums[i]
            counter[nums[i]] += 1

        if len(counter) >= m:            
            maxnum = num

        for i in range(k, len(nums)):
            num += nums[i]
            num -= nums[i-k]

            counter[nums[i]] += 1
            counter[nums[i-k]] -= 1
            
            if counter[nums[i-k]] == 0:
                del counter[nums[i-k]]

            if len(counter) >= m:
                maxnum = max(maxnum, num)
        
        return maxnum
