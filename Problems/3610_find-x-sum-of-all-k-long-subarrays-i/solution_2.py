class Solution(object):
    def findXSum(self, nums, k, x):
        """
        :type nums: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        
        n = len(nums)
        res = []

        for i in range(0, n-k+1):
            newNums = nums[i: i+k]
            
            mapp = {}
            for num in newNums:
                mapp[num] = mapp.get(num, 0) + 1
            
            minHeap = []

            for val, freq in mapp.items():
                item = (freq, val)
                if len(minHeap) < x:
                    heapq.heappush(minHeap, item)
                else:
                    heapq.heappushpop(minHeap, item)

            summ = 0
            
            for freq, val in minHeap:
                summ += freq * val
        
            res.append(summ)
            
        return res

            
                
            
            