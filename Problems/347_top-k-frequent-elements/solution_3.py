class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        
        items = []
        for num in count:
            items.append((count[num], num))
        items.sort(reverse=True)


        res = []
        for i in range(0, k):
            res.append(items[i][1])
        return res