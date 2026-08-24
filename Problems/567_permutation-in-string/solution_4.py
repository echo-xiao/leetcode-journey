class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)
        counter1 = defaultdict(int)
        counter2 = defaultdict(int)

        if k > n:
            return False
        
        for i in range(0, k):
            counter1[s1[i]] += 1
            counter2[s2[i]] += 1
        
        if counter1 == counter2:
            return True
        
        for i in range(k, n):
            counter2[s2[i]] += 1
            counter2[s2[i-k]] -= 1

            if counter2[s2[i-k]] == 0:
                del counter2[s2[i-k]]

            if counter1 == counter2:
                return True
        
        return False