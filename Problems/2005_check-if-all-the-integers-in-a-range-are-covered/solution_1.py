class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0] * 100
        for start, end in ranges:
            diff[start] += 1
            diff[end+1] -= 1

        cnt = 0
        for i in range(1, right+1):
            cnt += diff[i]
            if i >= left:
                if cnt == 0:
                    return False
        return True
        

        
        

