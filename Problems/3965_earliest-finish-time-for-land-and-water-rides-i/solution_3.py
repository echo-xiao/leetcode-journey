class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        i, j = 0, 0
        min_finish = float('inf')

        for i in range(0, len(landStartTime)):
            for j in range(0, len(waterStartTime)):
                land_finish = landStartTime[i] + landDuration[i]
                water_finish = waterStartTime[j] + waterDuration[j]

                total_finish1 = max(land_finish, waterStartTime[j]) + waterDuration[j]
                total_finish2 = max(water_finish, landStartTime[i]) + landDuration[i]
                
                curr = min(total_finish1, total_finish2)
                min_finish = min(min_finish, curr)

        return min_finish

