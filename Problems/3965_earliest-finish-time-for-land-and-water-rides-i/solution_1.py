class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:

        best = float('inf')
        for i in range(0, len(landStartTime)):
            for j in range(0, len(waterStartTime)):
                landFinishTime = landStartTime[i] + landDuration[i]
                waterFinishTime = waterStartTime[j] + waterDuration[j]                

                landFirstWaterSecond = max(landFinishTime, waterStartTime[j])
                optA = landFirstWaterSecond + waterDuration[j]
                
                waterFirstLandSecond = max(waterFinishTime, landStartTime[i])
                optB = waterFirstLandSecond + landDuration[i]

                curr = min(optA, optB)
                best = min(best, curr)
        return best