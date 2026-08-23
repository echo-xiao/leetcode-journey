class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        n = len(nums)
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        arr = []
        for i in range(0, n+1):
            arr.append([])

        for i in count:
            freq = count[i]
            arr[freq].append(i)

        res = []
        for i in range(n, -1, -1):
            for j in range(0, len(arr[i])):
                res.append(arr[i][j])
                if len(res) == k:
                    return res
        return res      
