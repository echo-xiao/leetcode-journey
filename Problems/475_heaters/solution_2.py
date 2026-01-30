class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        dis = []
        heaters.sort()
        for h in houses:
            leftDis = self.closestDistance(heaters, h, toLeft=True)
            rightDis = self.closestDistance(heaters, h, toLeft=False)
            dis.append(min(leftDis, rightDis))
        return max(dis)

    def closestDistance(self, heaters: List[int], h: int, toLeft: bool) -> int:
        left, right = 0, len(heaters)-1
        while left <= right:
            mid = left + (right - left) // 2
            if heaters[mid] == h:
                return 0
            elif heaters[mid] > h:
                right = mid - 1
            else:
                left = mid + 1
        
        if toLeft == True:
            if right < 0:
                return float('inf')
            return h - heaters[right]
        else:
            if left >= len(heaters):
                return float('inf')
            return heaters[left] - h