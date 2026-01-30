class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        delta = [0] * len(range(1950, 2100))

        curr = 0
        res = 0
        max_res = 0


        for birth, death in logs:
            delta[birth - 1950] += 1
            delta[death - 1950] -= 1        

        for i in range(len(delta)):
            curr += delta[i]

            if curr > max_res:
                max_res = curr
                res = i + 1950
        return res
            

        