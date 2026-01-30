class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        size = 0
        units = 0

        for i in range(0, len(boxTypes)):
            
            if size +  boxTypes[i][0] > truckSize:
                units += (truckSize - size) * boxTypes[i][1]
                break
            else:
                units += boxTypes[i][0] * boxTypes[i][1]
                size += boxTypes[i][0]

            i += 1

        return units