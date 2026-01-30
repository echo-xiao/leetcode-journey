class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        n = turnedOn 
        leds_values = [
            (1, 0), (2, 0), (4, 0), (8, 0),  # 小时
            (0, 1), (0, 2), (0, 4), (0, 8), (0, 16), (0, 32) # 分钟
        ]
        N = 10 
        

        dp = [[set() for _ in range(n + 1)] for _ in range(N + 1)]

        
        for i in range(N + 1):
            dp[i][0].add((0, 0))

        for i in range(1, N + 1):
            h_i, m_i = leds_values[i - 1]
            
            
            for j in range(1, n + 1):
                sums_without_i = dp[i - 1][j]
                
                
                sums_with_i = set()
                
                for (h, m) in dp[i - 1][j - 1]:
                    new_h, new_m = h + h_i, m + m_i
                    if new_h < 12 and new_m < 60:
                         sums_with_i.add((new_h, new_m))
                
                
                dp[i][j] = sums_without_i.union(sums_with_i)

        
        results = []
        for (h, m) in dp[N][n]:
            if h < 12 and m < 60:
                results.append(format_time(h, m))
                
        return results


from typing import List

def format_time(hour: int, minute: int) -> str:
    return f"{hour}:{minute:02d}"