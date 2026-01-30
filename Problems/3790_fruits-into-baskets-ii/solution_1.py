class Solution:
        
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        
        arr = [True] * len(baskets)
        cnt = 0

        for i in range(0, len(fruits)):
            for j in range(0, len(baskets)):
                if fruits[i] <= baskets[j] and arr[j] is True:
                    arr[j] = False
                    cnt += 1
                    break
        return len(baskets) - cnt
        


        