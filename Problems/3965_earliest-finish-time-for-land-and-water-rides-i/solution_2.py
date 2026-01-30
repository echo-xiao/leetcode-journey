class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_curr = float('inf')
        for i in range(0, len(landStartTime)):
            for j in range(0, len(waterStartTime)):
                land_finish = landStartTime[i] + landDuration[i]
                water_finish = waterStartTime[j] + waterDuration[j]

                res1 = max(land_finish, waterStartTime[j]) + waterDuration[j]
                res2 = max(water_finish, landStartTime[i]) + landDuration[i]

                curr = min(res1, res2)
                min_curr = min(min_curr, curr)
        return min_curr
