class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        left, right = 0, 0
        res = []
        while left < len(firstList) and right < len(secondList):
            low = max(firstList[left][0], secondList[right][0])
            high = min(firstList[left][1], secondList[right][1])

            if low <= high:
                res.append([low, high])
            if firstList[left][1] > secondList[right][1]:
                right += 1
            else:
                left += 1
        return res

            