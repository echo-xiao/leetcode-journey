class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]: 
        nums.sort()
        res = []
        
        for target in queries:
            sub = self.longestSubsequence(target, nums)
            res.append(sub)
        return res

    def longestSubsequence(self, target: int, nums: List[int]) -> int:
        ttl = 0
        length = 0

        for num in nums:
            if ttl + num <= target:
                ttl += num
                length += 1
            else:
                break
        return length
                
            

            